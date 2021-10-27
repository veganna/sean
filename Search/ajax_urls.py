from django.urls import path
from .ajax_views import *

app_name = "Ajax"

urlpatterns = [
    path('vehicle_type/', GetVehicleType, name ="vehicle_type"),
    path('make/', GetMake, name ="make"),
    path('model/', GetModel, name ="model"),
    path('year/', GetYear, name ="year"),
    path('category/', GetCategory, name ="category"),
    path('subcategory/', GetSubCategory, name ="subcategory"),
    path('brand/', GetBrand, name ="brand"),
]
