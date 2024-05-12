from . import views
from django.urls import path
from django.templatetags.static import static




urlpatterns = [

    path('',views.index,name='home'),
    path('product_list',views.Product_list,name='list_product'),
    path('product_detail/<pk>',views.Detail_product,name='detail_product')

]