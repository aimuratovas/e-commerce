from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Products.objects.all()
    data = {
        'products' : products,
    }
    return render(request, 'pages/index.html', data)

def all_categories(request):
    categories = []
    products = Products.objects.all()
    for product in products:
        categories.append(product.category)
    
    data = {
        'categories' : set(categories),
    }
    return render(request, 'pages/category.html', data)

def products_by_category(request, category):
    products = Products.objects.all().filter(category = category)
    data = {
        'products' : products,
    }
    return render(request, 'pages/products.html', data)

def product_info(request, name):
    product = Products.objects.all().filter(name = name)
    print(product[0].name)
    data = {
        'product_name' : product[0].name,
        'product_cost' : product[0].cost,
        'product_img' : product[0].img
    }
    return render(request, 'pages/product.html', data)
    
def search_by_name(request, name):
    # TODO
    render(request, 'pages/search_input.html')
    name = request.GET.get('name')

    product = Products.objects.all().filter(name = name)

    if not product:
        return render(request, 'pages/search_no_result.html')
    else:
        return product_info(request, name)


def shopping_cart(request):
    shoppings = Shopping_cart.objects.all()
    data = {
        'shoppings' : shoppings,
    }
    return render(request, 'pages/shopping_cart.html', data)