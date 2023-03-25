from django.shortcuts import render
from .models import Category, Products, Shop, Order

# Create your views here.

def home(request):
    products = Products.objects.all()
    category = Category.objects.all()

    context = {
        'products' : products,
        'category': category

    }
    return render(request, 'shop/home.html', context)