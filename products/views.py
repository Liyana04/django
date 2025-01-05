from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# django is the package, shortcut is the module importing render function
# Create your views here.

# /products -> index
def index(request):
    products = Product.objects.all()
    # return HttpResponse('hELLO WORLD')
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('new page WORLD')


