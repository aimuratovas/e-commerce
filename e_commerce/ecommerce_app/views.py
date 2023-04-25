from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    products = Products.objects.all()
    data = {
        'products': products,
    }
    return render(request, 'pages/index.html', data)


def all_categories(request):
    categories = []
    products = Products.objects.all()
    for product in products:
        categories.append(product.category)

    data = {
        'categories': set(categories),
    }
    return render(request, 'pages/category.html', data)


def products_by_category(request, category):
    products = Products.objects.all().filter(category=category)
    data = {
        'products': products,
    }
    return render(request, 'pages/products.html', data)


def product_info(request, name):
    product = Products.objects.all().filter(name__iexact=name)
    data = {
        'product': product[0]
    }
    return render(request, 'pages/product.html', data)


def search_by_name(request):
    name = request.GET.get("product_name")

    product = Products.objects.filter(name__iexact=name)

    if not product:
        return render(request, 'pages/search_no_result.html')
    else:
        return product_info(request, name)


def shopping_cart(request):
    shoppings = Shopping_cart.objects.all()
    total = 0
    for shopping in shoppings:
        print(shopping)
        print(shopping.product)
        total += shopping.product.cost * shopping.quantity
    data = {
        'shoppings': shoppings,
        'total': total
    }
    return render(request, 'pages/shopping_cart.html', data)


def add_shopping_cart(request, id):
    cart, created = Shopping_cart.objects.get_or_create(product_id=id)

    if not created:
        existing_quantity = cart.quantity
        cart.quantity = existing_quantity + 1
        cart.save()

    product = cart.product

    return render(request, 'pages/add_shopping_cart.html', {'product': product})
