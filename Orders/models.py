from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel
from localflavor.us.models import USStateField, USZipCodeField
from django.utils.translation import ugettext as _
from Login.models import AccountBase
from Products.models import Product


class Order(TimeStampedModel):
    address_1           = models.CharField("address 1", max_length=128)
    address_2           = models.CharField("address 2", max_length=128, blank=True)
    city                = models.CharField("city", max_length=64, default="Zanesville")
    state               = USStateField("state", default="OH")
    zip_code            = USZipCodeField("zip code", default="43701")
    user                = models.ForeignKey(AccountBase, on_delete=models.DO_NOTHING)
    is_paid             = models.BooleanField(default=False)
    is_complete         = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_price(self):
        total_cost = sum(item.get_total_price() for item in self.items.all())
        return total_cost

    def get_description(self):
        return ", ".join(
            [f"{item.quantity}x {item.product.name}" for item in self.items.all()]
        )


class Item(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(settings.CART_ITEM_MAX_QUANTITY),
        ]
    )

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return self.price * self.quantity