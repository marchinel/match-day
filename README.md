-- TUGAS 2 --

Tautan menuju aplikasi PWS:
https://naila-shafa41-matchday.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya memulai dengan membuat sebuah proyek Django baru dan memastikan lingkungan virtual sudah aktif agar dependensi proyek terpisah dengan sistem. Saya juga menambahkan requirements.txt yang berisi dependencies atau modul yang diperlukan. Setelah itu, saya melakukan konfigurasi environment variables dan proyek.

Setelah proyek dasar terbentuk, saya menambahkan sebuah aplikasi bernama main dan mendaftarkan aplikasi main ke dalam proyek melalui settings.py dengan menambahkannya ke dalam INSTALLED_APPS. 

Kemudian, saya membuat model bernama Product di dalam main/models.py. Model ini memiliki enam atribut wajib: name, price, description, thumbnail, category, dan is_featured dan melakukan migrasi database dengan perintah makemigrations dan migrate.

Setelah itu, saya membuat sebuah fungsi view di views.py yang bertugas mengembalikan sebuah template HTML. Template ini menampilkan informasi berupa nama aplikasi, serta nama dan kelas saya sendiri. Agar view tersebut dapat diakses, saya menambahkan sebuah routing di main/urls.py yang memetakan path root (/) ke fungsi view tadi. Selanjutnya, saya meng-include routing aplikasi main ke dalam urls.py di level proyek.

Terakhir, saya melakukan deployment dengan membuat project baru di PWS. Setelah project terbentuk, saya menambahkan URL deployment PWS ke dalam bagian ALLOWED_HOSTS di file settings.py. Selanjutnya, saya menambahkan remote repository PWS menggunakan perintah git remote add pws. Setelah itu, saya melakukan commit final, kemudian push ke branch utama dengan perintah git push pws main. Dengan langkah tersebut, aplikasi berhasil dideploy dan dapat diakses melalui URL yang disediakan PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

https://drive.google.com/file/d/1ZNNL6omANbZKICQ51nXboxt4y_K18-20/view?usp=sharing

urls.py berfungsi sebagai pengatur rute, yaitu menentukan ke mana sebuah request dari user akan diarahkan. Rute tersebut akan menuju ke fungsi atau kelas pada views.py, yang bertugas mengolah logika aplikasi. Jika membutuhkan data, views akan berinteraksi dengan models.py, yaitu bagian yang mengatur struktur data serta komunikasi dengan database. Setelah data diperoleh, views akan memilih template HTML yang sesuai, lalu menyisipkan data tersebut ke dalam tampilan. Hasil akhirnya berupa halaman web yang sudah berisi informasi lengkap, kemudian dikirim kembali kepada user.

3. Jelaskan peran settings.py dalam proyek Django!

Dalam proyek Django, file settings.py berperan sebagai pusat atau "otak" yang mengatur jalannya aplikasi, yaitu menentukan bagaimana aplikasi berjalan dan berinteraksi dengan pengguna maupun server. Semua konfigurasi penting, seperti informasi database, daftar aplikasi yang digunakan, middleware, keamanan (misalnya SECRET_KEY, DEBUG, dan ALLOWED_HOSTS), serta pengaturan file statis maupun media didefinisikan di dalamnya. Selain itu, settings.py juga memuat pengaturan bahasa, zona waktu, hingga konfigurasi tambahan seperti email dan logging.

4. Bagaimana cara kerja migrasi database di Django?

Migrasi database adalah menyinkronkan model Python dengan struktur tabel di database. Berikut cara kerjanya:
1) Menuliskan atau mengubah class model di models.py
2) Membuat file migrasi dengan code 'python manage.py makemigrations' yang kemudian Django akan membuat file migrasi berisi instruksi perubahan.
3) Menerapkan migrasi ke database dengan code 'python manage.py migrate' yang kemudian Django akan mengeksekusi file migrasi tadi dan menyesuaikan struktur database sesuai model.
4) Django menyimpan migrasi di tabel khusus (django_migrations) agar tahu migrasi mana saja yang sudah dijalankan.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sifatnya “batteries included” yang artinya Django sudah menyediakan banyak fitur dasar (autentikasi, ORM, admin panel, routing, dll.) tanpa perlu instalasi tambahan. Hal ini membuat pemula bisa langsung fokus memahami konsep inti pengembangan web, seperti model, view, controller, serta interaksi dengan database. Django juga memiliki dokumentasi yang lengkap dan komunitas yang besar, sehingga mudah dipelajari. Selain itu, Django menekankan struktur yang rapi, keamanan, dan skalabilitas, sehingga sejak awal mahasiswa atau pemula terbiasa dengan praktik terbaik dalam membangun aplikasi.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Untuk saya, tutorial 1 sangat membantu dan mudah dipahami.

-- TUGAS 3 --

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery adalah proses mengirimkan, mendistribusikan, dan menyajikan data dari satu titik ke titik lain, misalnya dari server ke pengguna. Data delivery penting dalam pengimplementasian platform adalah karena:
    - Platform berguna jika datanya bisa sampai ke pengguna, tanpa mekanisme pengiriman data, informasi akan terkunci di server dan tidak bisa dimanfaatkan.
    - Data delivery memungkinkan platform menyajikan informasi secara real-time.
    - Mekanisme data delivery yang baik akan memastikan setiap pengguna platform melihat data yang sama dan terbaru tanpa konflik.
    - Data delivery juga berkaitan dengan proteksi terhadap data saat dikirimkan agar data tidak hilang atau rusak saat dipindahkan.
    - Platform seringkali harus berkomunikasi dengan aplikasi lain, sehingga membutuhkan mekanisme data delivery yang standar agar integrasi bisa dilakukan.

2.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik, terutama dalam hal readability, kecepatan, serta keringanan yang membuat hemat bandwidth dan performa aplikasi lebih baik. Selain itu, JSON terintegrasi langsung dengan JavaScript yang sangat cocok untuk web API dan aplikasi web modern, serta didukung hampir semua framework modern. Kelebihan-kelebihan inilah yang membuat JSON lebih populer dibandingkan XML.  

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Untuk melakukan validasi terhadap data yang dikirim user sesuai dengan aturan yang sudah didefinisikan di form. Tanpa validasi, data yang masuk ke sistem bisa salah format, kosong padahal wajib, atau bahkan berbahaya.
Method is_valid() menyederhanakan proses validasi tersebut, sehingga kita tidak perlu menulis ulang logika validasi.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Tujuan csrf_token adalah untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Dengan token ini, Django bisa memastikan bahwa permintaan POST benar-benar berasal dari user yang sah melalui form dari website kita, bukan dari sumber lain yang berusaha menipu user.

Jika kita tidak menambahkan csrf_token, aplikasi jadi rentan terhadap CSRF karena server tidak bisa membedakan apakah request datang dari website asli atau dari situs berbahaya. Selain itu, user bisa tanpa sadar melakukan aksi berbahaya melalui program yang diam-diam mengirimkan request POST.

Ketiadaan csrf_token dimanfaatkan oleh penyerang dengan cara berikut:
    - Menyisipkan form palsu di website lain. Penyerang membuat form    HTML di situsnya yang kelihatannya tidak berbahaya. Saat korban yang sudah login di situs asli membuka situs penyerang, form palsu itu otomatis terkirim ke server asli menggunakan session korban.
    - Memanfaatkan session/cookie korban, karena browser otomatis mengirim cookie session saat mengakses domain asli, server menganggap request dari form palsu itu sah. Tanpa csrf_token, server tidak bisa mendeteksi bahwa request itu palsu.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya membuka berkas views.py pada app main dan menambahkan empat fungsi baru bernama show_xml, show_json, show_xml_by_id, dan show_json_by_id. Masing-masing fungsi saya buat untuk melakukan query ke model News, baik seluruh data maupun data berdasarkan id, kemudian hasilnya saya serialisasi menggunakan serializers.serialize() dan mengembalikannya dengan HttpResponse yang sudah saya atur content_type-nya menjadi "application/xml" atau "application/json" sesuai format yang dibutuhkan. 

Selanjutnya, saya mengatur routing dengan membuka urls.py, meng-import keempat fungsi tadi, lalu menambahkan path URL seperti xml/, json/, xml/<str:id>/, dan json/<str:id>/ ke dalam urlpatterns agar setiap view dapat diakses melalui endpoint masing-masing. Setelah itu saya menjalankan server Django dengan perintah python manage.py runserver, lalu menggunakan Postman untuk mengirim request GET ke keempat URL tersebut. Saya memastikan respon yang diterima sudah sesuai format XML maupun JSON, kemudian mengambil tangkapan layar dari setiap hasil, dan menambahkannya ke dalam berkas README.md sebagai dokumentasi.

Setelah itu, saya membuat kerangka template base.html di folder templates sebagai skeleton agar semua halaman memiliki desain yang konsisten. Saya memperbarui settings.py pada bagian TEMPLATES dengan menambahkan BASE_DIR / 'templates' ke dalam DIRS supaya base.html dapat dikenali sebagai template dasar.

Setelah itu, saya menyiapkan routing URL untuk setiap view. Pada berkas urls.py di app main, saya mengimpor fungsi show_main, create_product, dan show_product, lalu menambahkan path baru seperti path('', show_main, name='show_main'), path('create/', create_product, name='create_product'), dan path('product/<int:id>/', show_product, name='show_product') ke dalam urlpatterns agar halaman utama, form input, dan detail berita bisa diakses melalui URL masing-masing.

Langkah berikutnya, saya membuat halaman utama yang menampilkan daftar product. Saya mengubah main.html agar meng-extend base.html dan menampilkan data objek model menggunakan loop for. Di bagian atas halaman, saya menambahkan tombol “+ Add Product” yang mengarah ke URL create_product, sedangkan setiap item berita dilengkapi tautan judul dan tombol See Details menuju halaman detail show_product sesuai ID product.

Selanjutnya, saya menyiapkan halaman form untuk menambahkan objek model. Saya membuat forms.py dan mendefinisikan Product Form berbasis ModelForm. Di views.py saya menambahkan fungsi create_product yang memproses input form dan menyimpan data ke database ketika request adalah POST, serta merender template create_product.html jika belum disubmit. Saya juga menambahkan fungsi show_product untuk menampilkan detail berita dengan get_object_or_404 dan merender product_detail.html. Kedua template tersebut saya buat di folder main/templates untuk menampilkan form input dan detail berita.

Terakhir, saya menjalankan server dengan python manage.py runserver, menambahkan beberapa data product melalui form, dan menguji seluruh alur dari halaman utama, tombol Add Product, hingga halaman detail setiap product. Setelah melakukan beberapa penyesuaian tampilan web melalui main.html dan detail_product.html, saya melakukan add commit dan push ke GitHub maupun ke PWS.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada, tutorial 2 sudah jelas.

Screenshot dari hasil akses URL pada Postman
- XML: https://drive.google.com/file/d/1iP5bL9lv4v8huaLn2nu_Blq8BoSPEayO/view?usp=sharing
- json: https://drive.google.com/file/d/1qj5GQviIS2MOTFXaLMcH8IDYO6SU8EWG/view?usp=sharing

-- TUGAS 4 --

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan Django yang dipakai untuk proses login pengguna. Form ini disediakan oleh modul django.contrib.auth.forms. Secara default, AuthenticationForm menyediakan dua field utama, yaituusername dan password, serta otomatis melakukan validasi terhadap kredensial pengguna.

Ketika user mengisi username dan password, AuthenticationForm akan mengecek apakah user dengan username tersebut ada, memastikan password yang dimasukkan cocok dan memastikan akun aktif (bukan is_active=False).

Kelebihan:
    1. Sudah ada di Django. Tidak perlu menulis logika validasi dari nol.
    2. Integrasi dengan sistem auth Django yang langsung terhubung dengan model User dan mekanisme sesi (session).
    3. Keamanan terjamin dengan mendukung proteksi CSRF, hashed password, dan validasi standar yang aman.
    4. Mudah dikustomisasi dengan menambah field atau menyesuaikan tampilan lewat subclassing.

Kekurangan:
    1. Terbatas pada username/password. Jika ingin login dengan email, OTP, atau social login, perlu kustom tambahan.
    2. Tampilan standar sederhana dan butuh penyesuaian CSS/HTML agar sesuai desain.
    3. Validasi default kaku. Misalnya, pesan error bawaan mungkin perlu diubah untuk UX yang lebih ramah.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses untuk memverifikasi identitas pengguna, memastikan bahwa orang yang masuk ke sistem memang benar siapa yang ia klaim. Misalnya, saat pengguna mengisi username dan password, Django memeriksa kecocokan data dengan informasi yang tersimpan di database. Sedangkan otorisasi, terjadi setelah autentikasi berhasil. Proses ini menentukan hak akses pengguna, yaitu apa saja yang boleh dan tidak boleh dilakukan, seperti hanya admin yang dapat menghapus data atau mengubah pengaturan tertentu.

Django mengimplementasikan autentikasi melalui authentication framework bawaan (django.contrib.auth). Framework ini menyediakan model User untuk menyimpan data pengguna dengan password yang di-hash, fungsi authenticate() dan login() untuk memvalidasi kredensial, serta session middleware agar status login tersimpan antar permintaan (request). Setelah identitas diverifikasi, mekanisme otorisasi Django mengelola izin dengan sistem permissions dan groups, flag khusus seperti is_staff dan is_superuser, serta dekorator atau mixin seperti @login_required dan @permission_required. Dengan kombinasi ini, Django memastikan hanya pengguna yang sah dan memiliki hak yang tepat yang dapat mengakses atau memodifikasi sumber daya tertentu.
 
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies
Kelebihan:
    1. Sederhana & langsung di klien, data disimpan di browser, jadi server tidak perlu ruang tambahan.
    2. Bertahan lama dan bisa disetel agar tetap ada walau browser ditutup (misalnya untuk fitur “Remember Me”).
    3. Bisa diakses client-side, yaitu JavaScript dapat membaca atau mengubah nilai cookie jika diizinkan.
Kekurangan
    1. Keamanan lebih rentan, yaitu data berada di sisi klien, berpotensi dibaca atau dimodifikasi jika tidak di-encrypt dan tanpa flag HttpOnly/Secure.
    2. Ukuran terbatas, biasanya maksimal sekitar 4 KB per cookie.
    3. Overhead jaringan, Cookie ikut terkirim di setiap request/response, menambah beban trafik.

Session
Kelebihan:
    1. Lebih aman, lkarena data sensitif disimpan di server; browser hanya menyimpan ID session acak.
    2. Dapat menyimpan data besar/kompleks tidak dibatasi 4 KB seperti cookie.
    3. Integrasi mudah dengan autentikasi, cocok untuk login, keranjang belanja, dan data sementara lain.

Kekurangan:
    1. Membutuhkan penyimpanan server, butuh memori atau database untuk menyimpan session aktif.
    2. Masa hidup terbatas, biasanya berakhir ketika browser ditutup atau setelah timeout.
    3. Manajemen skala lebih rumit. Pada aplikasi multi-server perlu mekanisme session sharing (misalnya Redis).

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Penggunaan cookies tidak otomatis aman secara default, karena cookie disimpan di sisi klien (browser). Jika tidak dikonfigurasi dengan benar, cookie bisa menjadi titik lemah bagi serangan seperti session hijacking, cross-site scripting (XSS), atau cross-site request forgery (CSRF). Misalnya, cookie yang tidak di-encrypt dapat disadap melalui jaringan yang tidak aman, atau diakses JavaScript berbahaya jika tidak diberi flag HttpOnly. Cookie juga selalu terkirim bersama setiap request ke domain terkait, sehingga jika tidak dibatasi dengan SameSite atau Secure, bisa dimanfaatkan pihak ketiga.

Django mengantisipasi risiko ini dengan beberapa mekanisme bawaan. Saat menggunakan session berbasis cookie (django.contrib.sessions), Django hanya menaruh ID session yang di-sign di browser, bukan data sensitif langsung. Framework ini memverifikasi tanda tangan digital setiap cookie untuk mencegah pemalsuan. Selain itu, developer dapat mengaktifkan pengaturan keamanan seperti:
    - SESSION_COOKIE_SECURE = True agar cookie hanya terkirim melalui HTTPS.
    - SESSION_COOKIE_HTTPONLY = True agar cookie tidak bisa diakses JavaScript.
    - CSRF_COOKIE_SECURE dan CSRF_COOKIE_HTTPONLY untuk proteksi token CSRF.
    - SESSION_COOKIE_SAMESITE untuk mencegah pengiriman cookie lintas situs.

Dengan konfigurasi ini, Django memberi lapisan perlindungan yang kuat. Tetapi, keamanan tetap tergantung pada developer untuk memastikan opsi-opsi tersebut diaktifkan dan lingkungan server menggunakan HTTPS.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).