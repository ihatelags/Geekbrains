from django.shortcuts import render
import json
from mainapp.models import Product, ProductCategory

# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'Geekshop Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)