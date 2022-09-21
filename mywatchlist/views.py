from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchlistItems


def show_watchlist(request):
    pesan =''
    counter = 0
    watchlist_data = WatchlistItems.objects.all()

    for items in watchlist_data:
        if(items.movie_watched == "Yes"):
            counter+=1

    if(counter < 10 - counter):
        pesan="Wah, kamu masih sedikit menonton!"
    else:
        pesan="Selamat, kamu sudah banyak menonton!"

    context = {
        'watchlist_items': watchlist_data,
        'nama': 'Kristo Jeremy Thady Tobing',
        'npm': '2106633310',
        'pesan': pesan
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", watchlist_data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = WatchlistItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", watchlist_data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchlistItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")