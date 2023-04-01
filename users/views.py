from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, VendorSignUpForm
from shop.decorators import customer_required, vendor_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user'] = username
            # messages.info(request, f'You are now logged in as {request.user}')
            return redirect('home')
        else:
            messages.error(request, "Invalid username or Password")

    context = {}
    return render(request, 'registration/login.html', context)


def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form' : form,
    }
    return render(request, 'registration/signup.html', context)

@customer_required
def pre_vendor_signup(request, id):
    user = User.objects.get(request.user, id=id)

    if request.user.is_authenticated() and request.user.is_customer:
        messages.info(request, 'User wants to register as Vendor.')
        return redirect('vendor-signup')
    context = {}
    return render(request, 'registration/pre_vendor_signup.html', context)

@customer_required
def vendor_signup(request):
    form = VendorSignUpForm()

    if request.method == 'POST':
        form = VendorSignUpForm()

        if form.is_valid():
            form.save()
            vendor = form.cleaned_data.get('shop_owner')
            vendor_shop = form.cleaned_data.get('shop_name')
            messages.success(request, f'{vendor} + has created a shop + {vendor_shop}.')
            return redirect('vendor_dashboard')

    context = {
        'form' : form,
    }
    return render(request, 'registration/vendor_signup.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')