from . import views
from django.urls import path
from django.templatetags.static import static




urlpatterns = [

    path('cart',views.Show_Cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item'),
    path('checkout',views.chechout_cart,name='checkout'),
    path('orders',views.view_orders,name='orders'),



]