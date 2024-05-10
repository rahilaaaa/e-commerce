from django.shortcuts import render

# Create your views here.

def Show_Cart(request):
    return render(request,'cart.html')
