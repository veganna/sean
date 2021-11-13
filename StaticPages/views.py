from django.shortcuts import render
from Products.models import Category, Product
from .models import Contact

# Create your views here.

def Home(request):
    return render(request, 'pages/index.html')

def ContactUs(request):
    if request.method == 'POST':
        first_name = request.POST.get('Fname')
        last_name = request.POST.get('Lname')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Pnumber')
        question = request.POST.get('Question')
        instance = Contact(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number, question = question)
        instance.save()
        message = 'Thank You For Contact Us'
        return render(request, 'pages/contact.html', {'message':message})
    return render(request, 'pages/contact.html')

def About(request):
    return render(request, 'pages/about.html')