from django.contrib import admin

from Payments.models import Payment

from .models import Item, Order


class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ["product"]
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    can_delete = False
    readonly_fields = (
        "order",
        "transaction_amount",
        "Client_email",
        "Client_first_name",
        "Client_last_name",
        "created",
        "modified",
    )
    ordering = ("-modified",)

    def has_add_permission(self, request, obj):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__","zip_code", "state", "city" ,"address_1" ,"address_2" ,"user" ,"is_paid" ,"is_complete" ,"created" ,"modified"]
    list_filter = ["is_paid", "is_complete", "created", "modified"]
    search_fields = ["user"]
    inlines = [ItemInline, PaymentInline]