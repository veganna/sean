from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "user"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.add_input(
            Submit(
                "submit",
                "Checkout",
                css_class="btn btn-success btn-lg btn-block",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "",
                Div(
                    Field("zip_code", wrapper_class="col"),
                    Field("state", wrapper_class="col"),
                    Field("city", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("address_1", wrapper_class="col"),
                    Field("address_2", wrapper_class="col"),
                    Field("user", wrapper_class="col"),
                    css_class="row",
                ),
                css_class="border-bottom mb-3",
            )
        )