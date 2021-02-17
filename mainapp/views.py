from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None):
#     context = {
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#     return render(request, 'mainapp/products.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('-price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except:
        products_paginator = paginator.page(1)
    context = {
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
        }
    return render(request, 'mainapp/products.html', context)
