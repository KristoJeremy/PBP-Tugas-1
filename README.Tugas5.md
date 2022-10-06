# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Nama : Kristo Jeremy Thady Tobing

Kelas : PBP-D

NPM : 2106633310

## Link HEROKU 
http://localhost:8000/todolist

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Inline CSS  
Inline CSS dipakai untuk tag HTML tertentu dengan menambahkan atribut style secara langsung dalam tag HTML. Hal ini mengakibatkan semua elemen harus diberikan style secara manual. Namun, penggunaan CSS yang satu ini dapat berguna jika ingin mengakses CSS dengan cepat atau untuk styling file HTML yang kecil

* Internal CSS  
Internal CSS diletakan pada bagian head HTML. Elemen terkoneksi dengan CSS dengan atribut class atau id. Jika menggunakan metode ini maka perbuahan hanya terjadi pada satu halaman, dan secara langsung tidak memerlukan file css karena styling langsung dilakukan pada file HTML. Namun, umumnya metode ini mengingkatkan waktu akses website.

*  External CSS
External CSS akan menghubungkan HTML dengan file CSS yang terpisah, yang dihubungkan dengan linking href. Metode ini adalah lebih efisien terutama untuk styling file HTML besar karena kita hanya perlu memodifikasi external file saja. Salah satu kekurangnya metode ini adalah halaman belum tampil secara sempurna hingga file CSS selesai dipanggil

### Jelaskan tag HTML5 yang kamu ketahui.
* `<html>` tag untuk membuat dokumen HTML
* `<head>` tag untuk menempatkan metadata yang diperlukan
* `<title>` tag untuk membuat judul halaman
* `<body>` tag untuk menampung semua isi yang akan ditampilkan di web
* `<h1> - <h6>` tag untuk membuat heading
* `<p>` tag untuk mencetak text
* `<table>` tag untuk membuat tabel
* `<th>, <tr>, <td>` tag untuk membuat baris, cell header, dan cell dalam tabel.
* `<div>` : tag untuk membungkus sebuah bagian

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* Selektor tag, memilih berdasarkan nama tag
* Selektor Class, memilih berdasarkan nama class yang diberikan. 
* Selektor ID, hampir mirip dengan selektor class, tetepi ID harus unik atau tidak boleh ada yang sama diantara semua elemen
* Selektor atribut,  selektor yang memilih elemen berdasarkan atribut.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.**
* Untuk memodifikasi tampilan app website, saya menggunakan bootstrap. Pertama2, harus mempersiapkan styling dengan bootstrop dengan menambahkan pada head
```HTML
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```
* Serta menambahkan potongan kode berikut sebelum tag `</body>
```HTML
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```
* Untuk melakukan modifikasi menggunakan bootstrap, perlu mengimplementasikan menggunakan `class=""` styling yang terdapat pada dokumentasi bootstrap

**Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).**
* Logic yang saya terapkan dalam pebuatan card untuk masing-masing task adalah membuat satu card baru yang berisikan propertiesnya juga ketika forloop berjalan
```HTML
{% for task in list_task %}
    <div class="card text-white bg-primary mb-3 card text-center">
        <div class="card-body mb-4">
            <h4 class="card-title">{{task.title}}</h4>
                <p> Date : {{task.date}} </p>
                    <p> {{task.description}} </p>
                        {% if task.is_finished %}
                            <h5>Finished</h5>
                        {% else %}
                            <h5>Not Finished</h5>
                        {% endif %}
                        <button class="btn btn-light">
                            <a href="{% url 'todolist:finished_task' task.id %}">Finished</a>
                        </button>
                        <button class="btn btn-light">
                            <a href="{% url 'todolist:delete_task' task.id %}">Delete</a>
                        </button>
        </div>
    </div>
{% endfor %}
```

**Membuat keempat halaman yang dikustomisasi menjadi responsive.**
*Cara untuk membuat menjadi responsize adalah dengan menggunakan `<div> class = "container"" </div>`
