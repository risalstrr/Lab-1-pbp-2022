from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import barang_wishlist_xml
from wishlist.views import barang_wishlist_json
from wishlist.views import barang_wishlist_by_id_json
from wishlist.views import barang_wishlist_by_id_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', barang_wishlist_xml, name='barang_wishlist_xml'),
    path('json/', barang_wishlist_json, name='barang_wishlist_json'),
    path('json/<int:id>', barang_wishlist_by_id_json,
         name='barang_wishlist_by_id_json'),
    path('xml/<int:id>', barang_wishlist_by_id_xml,
         name='barang_wishlist_by_id_xml'),
]
