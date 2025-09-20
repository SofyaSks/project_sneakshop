from django import forms
from . import models
from .models import Sneaker,Color  

class FilterSortForm(forms.Form):

    brand = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices = [
            (b, b) for b in Sneaker.objects.values_list("brand", flat=True).distinct()
        ]
    )
    color = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices = [
            (c.id, c.name) for c in Color.objects.all().distinct()
        ]
    )
    sort = forms.ChoiceField(
        choices=[("lth", "From lowest to highest"), ("htl", "From highest to lowest")],
        required=False,
        widget=forms.RadioSelect)
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["brand"].choices = [
    #         (b, b) for b in Sneaker.objects.values_list("brand", flat=True).distinct()
    #     ]
    #     self.fields["color"].choices = [
    #         (c.id, c.name) for c in Color.objects.all().distinct()
    #     ]