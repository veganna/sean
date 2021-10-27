from django.urls import path
from .views import *

app_name='Pages'

urlpatterns = [
    path('', Home, name='home'),
    path('contact/', ContactUs, name='contact'),
    path('about/', About, name='about'),
]
