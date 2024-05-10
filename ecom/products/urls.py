from . import views
from django.urls import path
from django.templatetags.static import static




urlpatterns = [

    path('',views.index,name='home'),
    path('product_list',views.Product_list,name='list_product'),
    path('product_detail',views.Detail_product,name='detail_product')

]