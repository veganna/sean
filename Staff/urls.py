from django.urls import path
from .views import *
app_name='Staff'

urlpatterns = [
    path('', ExcelView, name='excel')
]
