from django.urls import path
from .views import *

app_name='Account'

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('register/', registrationPage, name="register"),
]