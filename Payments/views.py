
from decimal import Decimal
import json
from django.conf import settings
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from Orders.models import Order, shippmentOption
from .models import Payment
from Cart.cart import Cart

def export_request(request):
    return request

def PaymentMiddleware(order_id, client_email, client_first_name, client_last_name, request):
    total_amount = get_object_or_404(Order, id = order_id).get_total_price()
    shipping_cost = request.session['shippment_service']["shippmentCost"]
    shipping_cost = Decimal(shipping_cost)
    shipping_cost = round(shipping_cost, 2)
    shipping = shippmentOption(shippment_carrier=request.session['shippment_service']["serviceCode"],shippment_service_carrier = request.session['shippment_service']["serviceName"], shippment_cost = request.session['shippment_service']["shippmentCost"])
    shipping.save()
    total_amount = total_amount + shipping_cost
    
    order = get_object_or_404(Order, id = order_id)

    Order.objects.filter(id = order_id).update(is_paid=True)
    Payment.objects.create(order = order ,transaction_amount = total_amount, Client_email = client_email,  Client_first_name = client_first_name, Client_last_name = client_last_name, shippment=shipping )

def Payment_page(request):
    context = {}
    context['paypal_email_receive'] = settings.PAYPAL_EMAIL_RESEIVE
    context['paypal_client_id'] = settings.PAYPAL_CLIENT_ID
    context['paypal_secret_id'] = settings.PAYPAL_SECRET_ID
    context['shipmment_service'] = request.session['shipment_address']["carrier"]
    context['shipmment_service_name'] = request.session['shippment_service']["serviceName"]
    context['shipmment_service_code'] = request.session['shippment_service']["serviceCode"]
    context['shipmment_service_cost'] = request.session['shippment_service']["shippmentCost"]
    context['cart'] = Cart(request)
    
    def getOrder(request):
        order_id = request.session.get("order_id")
        order = get_object_or_404(Order, id=order_id)
        return order

    context['order'] = getOrder(request)
    return render(request, 'payment/payment.html', context)

@csrf_exempt
@require_POST
def PaymentSucess(request):
    body = json.loads(request.body)
    order_id = body['order_id']
    client_email = request.user.email
    client_first_name = request.user.first_name
    client_last_name = request.user.last_name
    PaymentMiddleware(order_id, client_email, client_first_name, client_last_name, request)
    return HttpResponseRedirect(reverse('Payment:success'))

def Payment_Success(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    cart = Cart(request)
    cart.clear()
    return render(request, "payment/success.html", {'order': order})



