from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
        'featured_products':featured_products,
        'latest_products':latest_products
    }


    return render(request,'index.html',context)


def Product_list(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    list_product = Product.objects.order_by('-priority')
    product_paginator = Paginator(list_product,7)
    list_product = product_paginator.get_page(page)
    context = {'products':list_product}
    return render(request,'product_layout.html',context)

def Detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product }
    return render(request,'product_detail.html', context)