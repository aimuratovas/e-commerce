from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), 
    path('category/', views.all_categories),
    path('category/<int:category_id>', views.products_by_category),
    path('product/<str:name>', views.product_info),
    path('shopping-cart/', views.shopping_cart),
    path('shopping-cart/<int:id>', views.add_shopping_cart),
    path('search/', views.search_by_name),
]

