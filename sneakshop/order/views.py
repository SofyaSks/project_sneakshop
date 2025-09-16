from django.shortcuts import render
from .models import Order, OrderSneaker
from .forms import OrderCreateForm
from cart.cart import Cart

def createOrder(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderSneaker.objects.create(
                    order = order, sneaker = item['sneaker']
                )
            cart.clear()
            return render(
            request,
            'order/created.html',
            {'order': order}
        )
    else:
        form = OrderCreateForm()           
        return render(
            request,
            'order/create.html',
            {'cart': cart, 'form': form}
        )


