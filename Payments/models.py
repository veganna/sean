
from django.db import models
from model_utils.models import TimeStampedModel

from Orders.models import Order


class Payment(TimeStampedModel):
    order                       = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_amount          = models.DecimalField("Transaction Amount", max_digits=10, decimal_places=2)
    Client_email                = models.EmailField()
    Client_first_name           = models.CharField(max_length=100) 
    Client_last_name            = models.CharField(max_length=100) 
    
    class Meta:
        ordering = ("-modified",)

    def __str__(self):
        return f"Payment {self.id}"
