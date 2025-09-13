from django import forms
from main.models import SneakerSize


class CartAddProductForm(forms.Form):

    size = forms.ModelChoiceField(
        queryset = SneakerSize.objects.none(), 
        to_field_name = 'id',
        empty_label = None
    )

    def __init__(self, *args, **kwargs):
        # pop удаляет ключ 'sneaker' из kwargs и возвращает его значение либо None.
        sneaker = kwargs.pop('sneaker', None)   # достаём sneaker из аргументов
        # Вызывает стандартную инициализацию формы Django
        super().__init__(*args, **kwargs)       # вызываем базовый конструктор
        if sneaker:                             # если передан конкретный кроссовок
            self.fields['size'].queryset = SneakerSize.objects.filter(sneaker=sneaker)

   
    