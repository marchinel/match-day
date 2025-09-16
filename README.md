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

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Screenshot dari hasil akses URL pada Postman
- XML: https://drive.google.com/file/d/1iP5bL9lv4v8huaLn2nu_Blq8BoSPEayO/view?usp=sharing
- json: https://drive.google.com/file/d/1qj5GQviIS2MOTFXaLMcH8IDYO6SU8EWG/view?usp=sharing
