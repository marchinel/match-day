from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all") 

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406356510',
        'name': request.user.username,
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

@login_required
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'is_product_popular': product.is_product_popular,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'is_product_popular': product.is_product_popular,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})
            return redirect("main:login")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                errors = [f"{field}: {error}" for field, errs in form.errors.items() for error in errs]
                return JsonResponse({"success": False, "error": errors[0] if errors else "Invalid input."})
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == 'POST':
        # kalau AJAX request, kita handle manual
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                response = JsonResponse({"success": True})
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({"success": False}, status=401)

        # kalau form biasa (non-AJAX), pakai AuthenticationForm
        else:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        logout(request)
        response = JsonResponse({"success": True})
        response.delete_cookie('last_login')
        return response
    
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product(request, id):
    try:
        product = Product.objects.get(pk=id)
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'description': product.description,
            'rating': product.rating,
            'is_featured': product.is_featured,
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
def edit_product(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id, user=request.user)
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.stock = request.POST.get('stock')
            product.category = request.POST.get('category')
            product.thumbnail = request.POST.get('thumbnail')
            product.save()
            return JsonResponse({'message': 'Product updated successfully'})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Unauthorized or product not found'}, status=403)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_product(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)

@login_required(login_url='/login')
def products_by_category(request, category):
    filter_type = request.GET.get("filter", "all") 

    if filter_type == "all":
        product_list = Product.objects.filter(category=category)
    else:
        product_list = Product.objects.filter(category=category, user=request.user)

    context = {
        "product_list": product_list,
        "last_login": request.COOKIES.get('last_login', 'never'),
    }
    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    rating = request.POST.get("rating")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'  # Checkbox handling
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        user=user,
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        stock=stock,
        rating=rating,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)