from django import forms
from . import models
from .models import Sneaker,Color, Size  

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
    size = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices = [
            (s.id, s.size) for s in Size.objects.all().distinct().order_by('size')
        ]
    )
    sort = forms.ChoiceField(
        choices=[("lth", "From lowest to highest"), ("htl", "From highest to lowest")],
        required=False,
        widget=forms.RadioSelect)
    
    