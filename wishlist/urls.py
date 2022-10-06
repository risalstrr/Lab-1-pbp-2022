from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import barang_wishlist_xml
from wishlist.views import barang_wishlist_json
from wishlist.views import barang_wishlist_by_id_json
from wishlist.views import barang_wishlist_by_id_xml
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import wishlist_ajax
from wishlist.views import add_wishlist_ajax

app_name = 'wishlist'

urlpatterns = [
     path('', show_wishlist, name='show_wishlist'),
     path('xml/', barang_wishlist_xml, name='barang_wishlist_xml'),
     path('json/', barang_wishlist_json, name='barang_wishlist_json'),
     path('json/<int:id>', barang_wishlist_by_id_json,
          name='barang_wishlist_by_id_json'),
     path('xml/<int:id>', barang_wishlist_by_id_xml,
          name='barang_wishlist_by_id_xml'),
     path('register/', register, name='register'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
     path('ajax/', wishlist_ajax, name="wishlist_ajax" ),
     path('ajax/submit/', add_wishlist_ajax, name="add_wishlist_ajax"),
]
