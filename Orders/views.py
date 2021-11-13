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


def Data_processor_json(lists):
    final_return = []
    for carrier in lists:
        if carrier:

            for quote in carrier:
                total = quote["otherCost"] + quote["shipmentCost"]
                quote["totalPrice"] = total
            sorted(carrier, key = lambda i: i['totalPrice'])
            final_return.append(carrier[-1])
    return final_return

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
    
def GetShippingRates(request):
    cart = Cart(request)
    weight = 0

    for item in cart:
        weight = weight + item["product"].product_weight
    
    data_Zipcode = request.GET.get("data-Zipcode")
    data_State = request.GET.get("data-State")
    data_City = request.GET.get("data-City")
    data_Address_1 = request.GET.get("data_Address_1")
    data_Address_2 = request.GET.get("data_Address_2")
    headers = {"content-type": "application/json"}
    
    data_Carrier = [{"serviceName":"fedex", "serviceCode":"fedex_home_delivery"},
    {"serviceName":"fedex", "serviceCode":"fedex_ground"},
    {"serviceName":"stamps_com", "serviceCode":"usps_priority_mail"}]

    list_service = []
    for item in data_Carrier:
        if request.GET.get("data-Zipcode") and request.GET.get("data-City") and request.GET.get("data_Address_1"):
            data = {
                "carrierCode": item["serviceName"],
                "serviceCode": item["serviceCode"],
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
                "confirmation": "delivery",
                "residential": True
            }
            r = requests.post('http://ssapi.shipstation.com/shipments/getrates', auth=(apikey, apisecret), data=json.dumps(data), headers=headers)
            if json.loads(r.text) not in list_service:
                list_service.append(json.loads(r.text))
        else:
            return JsonResponse({"error_service":"Error, Check your Address!"}, safe=False)
    
    if cart.get_total_price() >= 150:
        new_list = [{"totalPrice":0, "serviceName":"Free Shipping", "serviceCode":"free"}]
    else:
        new_list = Data_processor_json(list_service)
    
    shipment_context = {"data_Zipcode": data_Zipcode, "data_State": data_State, "data_City": data_City, "data_Address_1": data_Address_1, "data_Address_2": data_Address_2}
    request.session["shipment_context"] = shipment_context
    return JsonResponse(new_list, safe=False)

def UpdateTotalPrice(request):
    data_Service_code = request.GET.get("data_Price")
    data_Coust = request.GET.get("data_Service")
    shippment_service = {"serviceName": data_Service_code, "shippmentCost": data_Coust,}
    request.session["get_shipping_price"] = shippment_service
    return JsonResponse({"checked":'<i style="font-size:6rem; text-align:center; color:rgb(105, 189, 40);" class="fas fa-check"></i>'}, safe=False)

       