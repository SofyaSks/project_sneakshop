from django.conf import settings
from main.models import Sneaker, SneakerSize
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, sneaker_size, quantity = 1, override_quantity = False):
        sneaker_size_id = str(sneaker_size.id)
        if sneaker_size_id not in self.cart:
            self.cart[sneaker_size_id] = {'quantity':0,
                                     'price': str(sneaker_size.sneaker.price)}
        if override_quantity:
            self.cart[sneaker_size_id]['quantity'] = quantity
        else:
            self.cart[sneaker_size_id]['quantity'] += quantity     
        self.save()

    def remove(self, sneaker_size):
        sneaker_size_id = str(sneaker_size.id)
        if sneaker_size_id in self.cart:
            del self.cart[sneaker_size_id]
        self.save()

    def __iter__(self):
        sneaker_size_ids = self.cart.keys()
        sneaker_sizes = SneakerSize.objects.select_related('sneaker', 'size').filter(id__in=sneaker_size_ids)
        cart = self.cart.copy()
        for sneaker_size in sneaker_sizes:
            cart[str(sneaker_size.id)]['sneaker_size'] = sneaker_size
            cart[str(sneaker_size.id)]['sneaker'] = sneaker_size.sneaker
            cart[str(sneaker_size.id)]['size'] = sneaker_size.size
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
    


