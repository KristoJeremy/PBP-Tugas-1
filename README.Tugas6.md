# Tugas 6: Javascript dan AJAX

Nama : Kristo Jeremy Thady Tobing

Kelas : PBP-D

NPM : 2106633310

## Link HEROKU 
http://localhost:8000/todolist

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

* *Synchronous programming* adalah proses jalannya program secara sequential berdasarkan antrian eksekusi program. Hanya ada satu operasi yang bisa dijalankan pada satu waktu karena proses ini berjalan pada single-thread model. Karena eksekusi program dijalankan berdasarkan antrian, maka antrian proses harus diselesaikan terlebih dahulu sebelum eksekusi program yang lainnya. Maka dari itu, eksekusi bergantung pada keberhasilan yang dilakukan sebelumnya.

* *asynchronous programming* adalah operasi yang tidak bergantung pada eksekusi operasi lain, sehingga program lain dapat berjalan tanpa berganntung pada proses lain. Jenis program ini dapat menjalankan banyak eksekusi program sekaligus.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming merupakan paradigma dimana entitas (object, service, dll) dapat terintegrasi secara tidak langsung dengan mengirimkan event yang di-trigger oleh user.

## Penerapan asynchronous programming pada AJAX

AJAX mengimplementasikan cara untuk membuat halaman web app dapat diterbaharui secara asynchronous tergantung event yang di-trigger user. Hanya beberapa bagian dari halaman yang datanya berubah sedikit saja yang akan di-refresh, bukannya seluruh halaman web. AJAX dapat mengakses data dari sumber luar bahkan setelah halaman web dimuat seluruhnya.

## Cara implementasi checklist diatas

* Untuk mengimplementasikan checklist diatas perlu membuat dua fungsi pada `views.py`, yaitu untuk men-generate json dari database dan untuk menangkat input task baru dari user, masing2 terdapat pada fungsi `get_todolist_json` dan `add_todolist_ajax`

* Selanjutnya tambahkan url:
```py
path('json/', get_todolist_json, name='get_todolist_json'),
path('add/', add_todolist_ajax , name='add_todolist_ajax'),
```

* Selanjutnya, kita dapat mengubah html dengan menambahkan modal dan script. Pada bagian script terdapat fungsi `refreshContent` untuk menampilkan cards terupdate, fungsi `getTodolist` untuk fetch json, dan fungsi `addTask` untuk menambahkan task baru

