from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from Products.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product, quantity=cd["quantity"], override_quantity=cd["override"]
        )

    return redirect("Cart:detail")


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("Cart:detail")


def cart_detail(request):
    request.session["get_shipping_price"]={"shippmentCost":0}
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})