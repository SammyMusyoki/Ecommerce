from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Products, Shop, Order
from .forms import CreateProductForm, UpdateProductForm
from .decorators import customer_required, vendor_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    products = Products.objects.all()
    category = Category.objects.all()

    context = {
        'products' : products,
        'category': category

    }
    return render(request, 'shop/home.html', context)
@vendor_required
# @login_required(login_url='login')
def vendor_dashboard(request, pk):
    shop = Shop.objects.get()
    products = Products.objects.filter().order_by('-date')

    context = {
        'shop':shop
    }
    return render(request, 'shop/vendor/vendor_dashboard.html', context)


@vendor_required
# @login_required(login_url='login')
# Requires user to be logged in to create product and if user is_vendor
def create_product(request):
    form = CreateProductForm(request.POST)

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = Products.objects.create(**form.cleaned_data) 
            product.save()
            return redirect('home')

    context = {
        'form' : form
        }
    return render(request, 'shop/vendor/create_product.html', context)


@vendor_required
# @login_required(login_url='login')
# Requires user to be logged in to Update product and if user is_vendor
def update_product(request, id):
    product = get_object_or_404(Products, id=id)
    form = UpdateProductForm(instance=product)

    if request.method == 'POST':
        form = UpdateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form,
        }
    return render(request, 'shop/vendor/update_product.html', context)

# @login_required(login_url='login')
@vendor_required
# Requires user to be logged in to delete product and if user is_vendor
def delete_product(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request, 'shop/vendor/delete_product.html')