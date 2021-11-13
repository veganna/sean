from Products.models import ShippingAddress
from django.forms import ModelForm, fields
from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address_1','address_2','city','state','zip_code']
