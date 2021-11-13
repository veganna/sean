from django.urls import path
from .views import *
app_name = "Payment"

urlpatterns = [
    path('checkout/', Payment_page, name='checkout'),
    path('success/', Payment_Success, name='success'),
    path('payment-sucess/', PaymentSucess, name='sucess'),
]
