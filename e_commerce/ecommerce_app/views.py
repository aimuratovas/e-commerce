from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Products.objects.all()
    data = {
        'products' : products,
    }
    return render(request, 'pages/index.html', data)

def products_by_category(request, id):
    product = Products.objects.all().filter(id = id)
    data = {
        'product' : product,
    }
    return render(request, 'pages/pro.html', data)

def product_info(request, id):
    pass

def search_by_name(request, str):
    pass

def shopping_cart(request):
    shoppings = Shopping_cart.objects.all()
    data = {
        'shoppings' : shoppings,
    }
    return render(request, 'pages/shopping_cart.html', data)