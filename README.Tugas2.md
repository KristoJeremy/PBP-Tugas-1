# TUGAS 2
Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Nama : Kristo Jeremy Thady Tobing

Kelas : PBP-D

NPM : 2106633310

## Link HEROKU
Link: https://pbptugas2kristo.herokuapp.com/katalog/

## Bagan request client dan web app django
![](images/client%20req.png)

Request dimulai dari perintah user yang memasukkan url pada internet. Url yang telah diinput oleh user akan ditangkap oleh server Django dan kemudian akan diteruskan dalam source code yang telah dibuat. Url akan diproses pada urls.py dan jika sudah sesuai proses akan berlanjut ke views.py. Pada views.py terdapat fungsi yang mengintegrasikan models.py dan database dengan katalog.html sehingga dapat dibuatkan tampilan halaman. Dengan settings.py dan source code lainnya, halaman dapat ditampilan kepada user.

## Mengapa menggunakan virtual environment

Virtual enviroment adalah sebuah alat yang berfungsi untuk membuatkan lingkungan pemrograman terpisah yang diperlukan untuk berbagai proyek, seperti mengisolasi untuk masing-masing proyek. Misalkan saja terdapat dua proyek web dengan masing-masing menggunakan Django 1.9 dan yang lainnya Django 1.10, virtual environment akan berguna untuk mengisolasi kedua proyek. Selain itu, dengan adanya virtual environment, akan mencegah tercampurnya package yang digunakan dalam proyek dan package yang terdapat dalam host operating system. Jika tidak menggunakan virtual environment, maka tercampurnya package yang diperlukan proyek dan package default pada host. Package dapat overwritten dan menjadi rumit.

## Implementasi 

Pada views.py, pertama2 perlu melakukan import model (from katalog.models import CatalogItem) agar dapat mengakses models. Selanjutnya, diperlukan sebuah fungsi show_katalog yang melakukan query ke model database serta data tambahan dan mengaplikasikannya nanti dalam katalog.html 

def show_katalog(request):
    return render(request, "katalog.html", context)

context = {
    'list_barang': CatalogItem.objects.all(),
    'nama': 'Kristo Jeremy Thady Tobing',
    'npm': '2106633310'
}
  
Fungsi routing akan dilakukan pada urls.py pada folder katalog. Perlu melakukan import fungsi show_catalog from katalog.views import show_katalog. Selanjutnya, urls.py akan menangkap url dan memprosenya, ketika url katalog terpanggil maka show_katalog akan dijalankan.

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog')
]

Selain itu perlu juga menambahkan (path('katalog/', include('katalog.urls'))) pada urls.py di folder django project
  
Pada katalog.html perlu ada tambahan untuk menampilkan informasi nama (<b>{{nama}}</b>) dan npm  (<b>{{npm}}</b>). Selain itu, perlu ada syntax di dalam tabel yang berfungsi untuk mencetak item2 dan informasi yang terdapat dalam file json. 

{% for barang in list_barang %}
      <tr>
          <th>{{barang.item_name}}</th>
          <th>{{barang.item_price}}</th>
          <th>{{barang.item_stock}}</th>
          <th>{{barang.rating}}</th>
          <th>{{barang.description}}</th>
          <th>{{barang.item_url}}</th>
      </tr>
    {% endfor %}
    
Untuk melakukan deployment, ada beberapa tambahan untuk source code. Dalam settings.py perlu menambahkan 

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

dan pada middleware perlu menambahkan 

'whitenoise.middleware.WhiteNoiseMiddleware',
  
Pada tahap ini, semua implementasi pada source code sudah tuntas. Selanjutnya perlu dilakukan commmit dan push, action, dan melakukan deploy pada heroku


