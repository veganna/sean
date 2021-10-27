from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from Cart.cart import Cart
from django.http import JsonResponse
from .forms import OrderCreateForm
from .models import Item, Order
from core.settings import SHIPPING_API_Key as apikey, SHIPPING_API_Secret as apisecret
import requests
import json
from decimal import Decimal



class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            for item in cart:
                Item.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            self.request.session["order_id"] = order.id
            return redirect(reverse("Payment:checkout"))
        return redirect(reverse("Pages:home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context



def GetCarrier(request):
    data_value = request.GET.get("data-Value")
    r = requests.get('http://ssapi.shipstation.com/carriers', auth=(apikey, apisecret))
    data_value = json.loads(r.text)
    return JsonResponse( data_value, safe=False)
    
def GetShippingRates(request):
    cart = Cart(request)
    weight = 0
    lenght = 0
    width = 0
    height = 0
    items = 0
    
    for item in cart:
        items = items + 1
        weight = weight + item["product"].product_weight
        lenght = lenght + item["product"].product_lenght
        width = width + item["product"].product_width
        height = height + item["product"].product_height

    lenght = lenght/items
    width = width/items
    height = height/items

    data_Carrier = request.GET.get("data-Carrier")
    data_Zipcode = request.GET.get("data-Zipcode")
    data_State = request.GET.get("data-State")
    data_City = request.GET.get("data-City")
    data_Address_1 = request.GET.get("data_Address_1")
    data_Address_2 = request.GET.get("data_Address_2")
    headers = {"content-type": "application/json"}
    data = {
        "carrierCode": data_Carrier,
        "serviceCode": None,
        "packageCode": None,
        "fromPostalCode": "33770",
        "toState": data_State,
        "toCountry": "US",
        "toPostalCode": data_Zipcode,
        "toCity": data_City,
        "weight": {
          "value": str(weight),
          "units": "pounds"
        },
        "dimensions": {
          "units": "inches",
          "length": str(lenght),
          "width": str(width),
          "height": str(height)
        },
        "confirmation": "delivery",
        "residential": True
    }
    if request.GET.get("data-Zipcode") and request.GET.get("data-City") and request.GET.get("data_Address_1"):
        r = requests.post('http://ssapi.shipstation.com/shipments/getrates', auth=(apikey, apisecret), data=json.dumps(data), headers=headers)
        data_value = json.loads(r.text)
        if request.GET.get("data_Address_2"):
            shipment_address = {"State": data_State, "zipCode": data_Zipcode, "City": data_City, "Address_1": data_Address_1, "Address_2": data_Address_2, "carrier":data_Carrier}        
        else:
            shipment_address = {"State": data_State, "zipCode": data_Zipcode, "City": data_City, "Address_1": data_Address_1, "carrier":data_Carrier}
        
        request.session["shipment_address"] = shipment_address 
    else:
        return JsonResponse({"error_service":"Error, Check your Address!"}, safe=False)
    return JsonResponse(data_value, safe=False)

def UpdateTotalPrice(request):
    data_Service_carrier = request.GET.get("data_Service-carrier")
    data_Service_code = request.GET.get("data_Service-code")
    data_Coust = request.GET.get("data_Shipping-cost")
    shippment_service = {"serviceCode": data_Service_code, "shippmentCost": data_Coust, "serviceName": data_Service_carrier}
    request.session["shippment_service"] = shippment_service
    return JsonResponse({"checked":'<i style="font-size:6rem;" class="fas fa-check"></i>'}, safe=False)


