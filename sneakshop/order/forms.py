from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField 

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'name', 'email']

    

