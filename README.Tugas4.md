# TUGAS 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama : Kristo Jeremy Thady Tobing

Kelas : PBP-D

NPM : 2106633310

## Link HEROKU 
http://localhost:8000/todolist 
{
## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Sebuah serangan Cross-Site Request Forgery (CSRF) memaksa web application untuk melakukan perintah-perintah yang tidak diinginkan pada device pengguna. Attackers menggunakan user's authenticated state untuk mengganti request user dengan perintah-perintah yang tidak seharusnya dijalankan.

Django menyediakan sebuah implementasi untuk mencegah terjadinya serangan ini. Serangan ini dapat ditangkal dengan `{% csrf_token %}`. Implementasi ini menggunakan token sebagai syarat untuk melakukan request. Token ini bersifat unik, rahasia, dan sulit untuk ditebak. Jika tanpa menggunakan token tersebut, attackers bisa saja melakukan request yang berbahaya dengan akun user anda, contoh saja penyadapan ketika sedang melakukan transfer uang melalui web application. Namun, jika menggunakan token tersebut, attackers akan sulit untuk menebak token dan tidak mungkin melakukan request.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Handling forms adalah sesuatu yang cukup rumit. Django form dapat memudahkan pembuatan dan pemodelan form. Django dapat menyiapkan dan menstrukturisasi data sehingga bisa render, membuat HTML forms, serta menerima dan memproses data. 

Akan tetapi, pembuatan forms sangat bisa untuk dikembangkan secara manual. Hal ini dapat dilakukan dengan menggunakan `<form>` sebagai wrapper dan memberikan atribut yang dibutuhkan dalam `method` dan `action`. Atribut  `method` digunakan untuk menentukan cara untuk mengirimkan form-data dan `action` akan menentukan kemana lokasi penyimpanan pengirimnan form-data setelah form disubmit. Kita dapat menyesuaikan tipe input yang kita perlukan. Selanjutnya, kita dapat memberikan atribut `name` untuk menentukan nama dan reference form data. Dan untuk menjalankan form, dapa tiberikan elemen `button`.

## Jelaskan alur data dari submisi pengguna melalui HTML form, penyimpanan data dari database, sampai munculnya data yang telah disimpan pada template HTML
Ketika user klik button submit yang telah terhubung dengan def yang dapat menerima request, tampilan HTML, dan user input pada views.py. Data yang telah disubmit dapat ditampilkan pada dengan bantuan def shwo_task.

## Implementasi Checklist
* Buatlah aplikasi `todolist`. Kemudian pada `project_django` masukan aplikasi pada `installed_apps` pada `settings.py` dan tembahkan pula path pada `urls.py`.
* Pada `models.py` buatlah fungsi yang berisikan artibut username, date, title, description, dan status valid
* Pada `views.py` buat fungsi untuk menampilkan tampilan utama serta buat pula fungsi untuk mengimplementasikan login, register, logout, create task, change status, dan delete task
* Buat file baru bernama `forms.py`untuk handle membuat form penambahan task
* Membuat empat file HTML masing-masing untuk halaman todolist, login, register, dan create task
* Membuat routing path pada `urls.py` dengan menambahkan url baru pada urlpatterns
* Melakukan cek pada menggunakan `localhost`
* Jika sudah selesai, lakukan add, commit, dan push pada repository github dan deployment akan terjadi secara otomatis.
