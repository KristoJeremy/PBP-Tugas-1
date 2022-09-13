from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    return render(request, "katalog.html", context)

context = {
    'list_barang': CatalogItem.objects.all(),
    'nama': 'Kristo Jeremy Thady Tobing',
    'npm': '2106633310'
}