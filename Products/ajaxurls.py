from django.urls import path
from .ajaxviews import *

urlpatterns = [
    path('vehicle-land/', GetVehicleLand, name='vland'),
    path('vehicle-type/', GetVehicleType, name='vtype'),
    path('category/', GetCategory, name='category'),
    path('sucategory/', GetSubcategory, name='subcategory'),
    path('submit/', Submit, name='submit'),
    path('product_identify/', ProductIdentifier, name='identify'),
]
