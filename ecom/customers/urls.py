from . import views
from django.urls import path
from django.templatetags.static import static




urlpatterns = [

    path('account',views.Account,name='account'),

]