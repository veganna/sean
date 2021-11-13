from django.urls import path
from .views import *

app_name = "Orders"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create"),
    path("GetRates/", GetShippingRates, name="GetRates"),
    path("Update_price/", UpdateTotalPrice, name="update_price")
]
