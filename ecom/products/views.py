from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def Product_list(request):
    return render(request,'product_layout.html')

def Detail_product(request):
    return render(request,'product_detail.html')