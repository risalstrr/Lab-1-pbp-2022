from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers


def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Risa'
    }
    return render(request, "wishlist.html", context)

# Mengembalikan Data dalam Bentuk XML


def barang_wishlist_xml(request):
    data_barang = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_barang), content_type="application/xml")

# Mengembalikan Data dalam Bentuk JSON


def barang_wishlist_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Mengembalikan Data dalam Bentuk XML Berdasarkan id


def barang_wishlist_by_id_xml(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Mengembalikan Data dalam Bentuk JSON Berdasarkan id


def barang_wishlist_by_id_json(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
