from . import views
from django.urls import path
from django.templatetags.static import static




urlpatterns = [

    path('cart',views.Show_Cart,name='cart'),

]