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