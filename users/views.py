from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('shop:home')
    else:
        form = SignUpForm()

    context = {
        'form' : form
    }
    return render(request, 'registration/signup.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {user.last_name} {user.firstname}')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or Password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)