from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models import SneakerSize, Sneaker

class Order(models.Model):
    phone = PhoneNumberField(region = 'CA')
    name = models.CharField(max_length=15)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class OrderSneaker(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    size = models.ForeignKey(SneakerSize, on_delete=models.CASCADE)



