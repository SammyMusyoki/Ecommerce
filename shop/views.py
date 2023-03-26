from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Products, Shop, Order
from .forms import CreateProductForm, UpdateProductForm

# Create your views here.

def home(request):
    products = Products.objects.all()
    category = Category.objects.all()

    context = {
        'products' : products,
        'category': category

    }
    return render(request, 'shop/home.html', context)

def vendor_shop(request, pk):
    shop = Shop.objects.get()

    context = {
        'shop':shop
    }
    return render(request, 'shop/vendor_shop.html', context)


def create_product(request):
    form = CreateProductForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form
        }
    
    return render(request, 'shop/create_product.html', context)

def update_product(request, pk):
    data = get_object_or_404(Products, id=pk)
    form = UpdateProductForm(instance=data)

    if request.method == 'POST':
        form = UpdateProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form
        }
    return render(request, 'shop/create_product.html', context)