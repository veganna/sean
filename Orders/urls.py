from django.urls import path
from .views import *

app_name = "Orders"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create"),
    path("getcarrier/", GetCarrier, name="carrier"),
    path("getshippingrates/", GetShippingRates, name="rates"),
    path("upgrade_total/",UpdateTotalPrice, name="shppingCost"),
]