# TUGAS 3
Pengimplementasian Data Delivery Menggunakan Django

Nama : Kristo Jeremy Thady Tobing

Kelas : PBP-D

NPM : 2106633310

## Link HEROKU
Link HTML: https://pbptugas2kristo.herokuapp.com/mywatchlist/html/

Link XML: https://pbptugas2kristo.herokuapp.com/mywatchlist/xml/

Link JSON: https://pbptugas2kristo.herokuapp.com/mywatchlist/json/

## Perbedaan antara JSON, XML, dan HTML
**JSON** atau JavaScript Object Notation adalah sebuah format yang berfungsi untuk menyimpan, mambaca, dan menukar informas web server sehingga dapat dibaca oleh user. Hampir sama dengan **JSON**, **XML**  atau Extensible Markup Language juga berfungsi sebagai pertukaran data serta menyimpan dan menampilakannya. Terdapat pula **HTML** atau HyperText Markup Language. Berbeda daripada **JSON** atau **XML**, yang lebih berorientasi pada strukturisasi data dan dokumennya, **HTML** lebih berorientasi kepada penggambaran konten halaman aplikasi.

Jika dilihat dari perbandingannya, maka lebih mudah untuk membandingkan **JSON** dan **XML**. **JSON** hanyalah sabuh format data sedangkan **XML** adalah bahasa markup. **XML** dapat digunakan untuk menyimpan dan mengangkut data sedangkan **JSON** lebih cocok untuk pertukaran data ringan yang lebih mudah diurai oleh komputer. Dari sisi readibility maka **JSON** daripada **XML**.

## Mengapa kita memerlukan data delivery dalam pengimplementasian platform
Data delivery sangat penting dalam pembuatan suatu platform dikarenakan data yang terdapat pada **JSON** atau **XML** akan menjadi sebuah acuan database bagi aplikasi web. Selain itu, web membutuhkan sebuah kode acuan sebuah tampilan yang dapat diatur dalam **HTML**. Data delivery berfungsi sebagai penyimpanan data, transfer data, dan menampilkan data pada aplikasi web

## Cara pengimplementasian checklist
* Pertama-tama, kita harus membuat aplikasi baru di repo local project django lanjutan tugas 2 sebelumnya, dapat dilakukan dengan menjalankan command 

```py 
python manage.py startapp mywatchlist
```
* Maka akan terbuat sebuah folder aplikasi baru bernama mywatchlist 
* Lalu aktifkan terlebih dahulu url http://localhost:8000/mywatchlist dengan cara menambahkan potongan kode berikut pada urls.py di project_django
```py
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls'))
]
```
* Tidak lupa juga untuk mendaftarkan aplikasi pada settings.py
```py
INSTALLED_APPS = [
   ...
    'mywatchlist'
]
```
* Sekarang, kita dapat memulai untuk membuat proses data delivery. Pada models.py, kita membuat class yang berisikan tipe-tipe data yang akan ditampilkam
``` py
class WatchlistItems(models.Model):
    movie_watched = models.TextField()
    movie_title = models.TextField()
    movie_rating = models.IntegerField()
    movie_release_date = models.TextField()
    movie_review = models.TextField()
```
* Lalu, buatlah folder bernama fixtures pada folder aplikasi, lalu buatlah database dengan nama initial_watchlist_data.json dan diisi dengan
``` json
[
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 1,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "The Green Mile",
            "movie_rating": 8.6,
            "movie_release_date": "December 16, 1999",
            "movie_review": "The Green Mile is a masterwork. This is film as art, at it's very best. The depth of the cast is extraordinary, with all of the players delivering excellent performances."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 2,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "American Pie",
            "movie_rating": 7.0,
            "movie_release_date": "July 9, 1999",
            "movie_review": "American Pie is a fairly good movie,with good humor and a funny storyline,its a total teenage movie but its better than average ones."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 3,
        "fields": {
            "movie_watched": "Not yet",
            "movie_title": "The Samaritan",
            "movie_rating": 5.7,
            "movie_release_date": "August 26, 2022",
            "movie_review": "Really have no clue to the thinking behind movies like this, it's like watching a really bad live action cartoon,"
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 4,
        "fields": {
            "movie_watched": "Not yet",
            "movie_title": "T-34",
            "movie_rating": 9.5,
            "movie_release_date": "January 1, 2019",
            "movie_review": "Performances are amazing, production design is amazing, cinematography is amazing, editing, effects, and story is uber compelling."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 5,
        "fields": {
            "movie_watched": "Not yet",
            "movie_title": "The Pianist",
            "movie_rating": 9.5,
            "movie_release_date": "September 6, 2002",
            "movie_review": "Man, I can not get this film out of my head. It is so rare that a movie can affect me the way 'The Pianst' did."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 6,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "Brothers",
            "movie_rating": 8.0,
            "movie_release_date": "June 1, 2010",
            "movie_review": "Brothers is a decent movie showing the trauma both a soldier and his family face due to Tobey Maguire's 'job' as a marine."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 7,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "Begin Again",
            "movie_rating": 8.5,
            "movie_release_date": "June 27, 2014",
            "movie_review": "This movie helped me get through a phase in a life and definitely helped me .love it yes it has its flows but whatever."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 8,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "Hesher",
            "movie_rating": 8.3,
            "movie_release_date": "May 13, 2011",
            "movie_review": "Simply put, Hesher is an exploration of loss: a universal experience shared by the film's characters"
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 9,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "Easy A",
            "movie_rating": 8.0,
            "movie_release_date": "September 17, 2010",
            "movie_review": "What drew me to this film were the cast, on paper this was a great cast capable of great performances."
        }
    },
    {
        "model": "mywatchlist.watchlistitems",
        "pk": 10,
        "fields": {
            "movie_watched": "Yes",
            "movie_title": "Bad Boys II",
            "movie_rating": 9.0,
            "movie_release_date": "August 6, 2003",
            "movie_review": "This movie kicked ass plain and simple."
        }
    }
]
```
* Untuk dapat mengakses dalam bentuk json, html, atau xml kita perlu membuat class baru pada views.py
```py
def show_watchlist(request):
    watchlist_data = WatchlistItems.objects.all()
    return render(request, "watchlist.html", context)

def show_xml(request):
    watchlist_data = WatchlistItems.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist_data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = WatchlistItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    watchlist_data = WatchlistItems.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist_data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchlistItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
* Kemudian pada urls.py, tambahkan url untuk membuat routing json, html, atau xml
```py
app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_watchlist, name='show_watchlist'), 
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id')
]
```
* Pada procfile tambahkan potongan kode berikut
```py
... && python manage.py loaddata initial_watchlist_data.json
```
* Setelah melakukan semua langkah diatas tidak lupa untuk mengkatifkan env, makemigrations, migrate, loaddata, dan runserver. Maka aplikasi sudah dapat berjalan pada localhost
* Lakukan deployment. Add, commit, lalu push ke github dengan repositori yang sama dengan tugas 2, maka workflow akan berjalan otomatis dan sinkron dengan app pada heroku
* Tidak lupa juga untuk menambahkan test unit untuk ketiga url pada test.py
```py
class TestUrl(TestCase):
    def test_html(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
```

## Screenshot postman
![Screenshot (1366)](https://user-images.githubusercontent.com/112571178/191628912-37d8bbd8-ebb9-44a2-b0b1-8a9a691f8706.png)
![Screenshot (1367)](https://user-images.githubusercontent.com/112571178/191628923-9679ef06-cdf4-4f21-b5a1-0f1289b4473e.png)
![Screenshot (1368)](https://user-images.githubusercontent.com/112571178/191628926-8b808bba-31a5-43de-96bd-3ca27667d5a3.png)



