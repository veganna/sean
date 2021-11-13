
import json
from django.conf import settings
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from Orders.models import Order
from .models import Payment
from Cart.cart import Cart

def getOrder(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    return order

def PaymentMiddleware(order_id, client_email, client_first_name, client_last_name, cart):
    total_amount = cart.get_total_price()
    order = get_object_or_404(Order, id = order_id)
    print(order)
    Order.objects.filter(id = order_id).update(is_paid=True)
    Payment.objects.create(order= order ,transaction_amount = total_amount, Client_email = client_email,  Client_first_name = client_first_name, Client_last_name = client_last_name )

def Payment_page(request):
    cart = Cart(request)
    context = {}
    context['paypal_email_receive'] = settings.PAYPAL_EMAIL_RESEIVE
    context['paypal_client_id'] = settings.PAYPAL_CLIENT_ID
    context['paypal_secret_id'] = settings.PAYPAL_SECRET_ID
    context['shipping_price'] = request.session['get_shipping_price']["shippmentCost"]
    context['service_name'] = request.session['get_shipping_price']["serviceName"]
    context['total_price_after_shipping'] = cart.get_total_price()
    context['order'] = getOrder(request)
    return render(request, 'payment/payment.html', context)

@csrf_exempt
@require_POST
def PaymentSucess(request):
    cart = Cart(request)
    body = json.loads(request.body)
    order_id = body['order_id']
    client_email = request.user.email
    client_first_name = request.user.first_name
    client_last_name = request.user.last_name
    PaymentMiddleware(order_id, client_email, client_first_name, client_last_name, cart)
    return HttpResponseRedirect(reverse('Payment:success'))

def Payment_Success(request):
    cart = Cart(request)
    cart.clear()
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    return render(request, "payment/success.html", {'order': order})



