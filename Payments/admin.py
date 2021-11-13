
from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "order",
        "transaction_amount",
        "Client_email",
        "Client_first_name",
        "Client_last_name",
        "created",
        "modified",
    ]
    list_filter = ["modified"]
    search_fields = ["Client_email", "Client_first_name", "Client_last_name",]
