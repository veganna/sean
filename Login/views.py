from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from Cart.cart import Cart
from .models import *
from .forms import *


#login cyrcle views


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            path = request.POST.get('path')
            if path:
                return redirect(path)
    return redirect('Pages:home')

def logoutPage(request):
    logout(request)
    return redirect('Pages:home')


def registrationPage(request):
    cart = Cart(request)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if cart:
                    return redirect('Orders:create')
                return redirect('Pages:home')
        else:
            form = RegistrationForm()
            message = 'try again!'
            return render(request, 'account/registration.html', {'registration': form, 'message':message})
    return render(request, 'account/registration.html', {'registration': form})




