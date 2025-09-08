from django import forms
from main.models import SneakerSize

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1,6)]

class CartAddProductForm(forms.Form):
    size_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.TypedChoiceField(
        choices = PRODUCT_QUANTITY_CHOICES,
        coerce = int
    )

    override = forms.BooleanField(required=False,
                                  initial = False,
                                  widget=forms.HiddenInput)
    
    