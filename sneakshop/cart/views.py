from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Sneaker, SneakerSize
from . cart import Cart
from . forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        size_id = cd['size_id']
        sneaker_size = get_object_or_404(SneakerSize, id = size_id, sneaker_id = product_id)
        cart.add(sneaker_size=sneaker_size, quantity=cd['quantity'], 
                 override_quantity=cd['override'])
    return redirect('cart')

@require_POST
def cart_remove(request, size_id):
    cart = Cart(request)
    sneaker_size = get_object_or_404(SneakerSize, id = size_id)
    cart.remove(sneaker_size)
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    return render(
        request,
        'cart/cart.html',
        {
            'cart': cart
        }
    )
