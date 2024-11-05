from django.shortcuts import render
from . models import Product
# Create your views here.
from django.http import HttpResponse
def index(request):
 return HttpResponse("Index Blog")

def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"shop/index.html", params)

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/basic.html')


def contact(request):
    return HttpResponse("We are contact")


def tracker(request):
    return HttpResponse("We are tracker")


def search(request):
    return HttpResponse("We are search")


def prodView(request):
    return HttpResponse("We are view")


def checkout(request):
    return HttpResponse("We are checkout")

