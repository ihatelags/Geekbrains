from django.shortcuts import render
import json


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    with open('mainapp/templates/mainapp/products.json', encoding='utf-8-sig') as f:
        data = json.load(f)
    context = {
        'title': 'GeekShop - каталог',
        'categories': [
            {'name': 'одежда', 'href': '#'},
            {'name': 'обувь', 'href': '#'},

        ],
        'products': data,
    }

    return render(request, 'mainapp/products.html', context=context)