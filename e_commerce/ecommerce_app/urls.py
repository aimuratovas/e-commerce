from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), 
    path('category/<int:id>', views.products_by_category),
    path('product/<int:id>', views.product_info),
    path('shopping-cart/', views.shopping_cart),
    path('search/<str:search>', views.search_by_name), #TODO
]

