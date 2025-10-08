from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, ajax_login, ajax_register, edit_product, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),  
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('ajax/login/', ajax_login, name='ajax_login'),
    path('ajax/register/', ajax_register, name='ajax_register'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product')
]
