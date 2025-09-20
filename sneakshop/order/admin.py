from django.contrib import admin
from . import models

@admin.register(models.Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['phone', 'name', 'email', 'created', 'paid']

@admin.register(models.OrderSneaker)
class AdminOrderSneaker(admin.ModelAdmin):
    list_display = ['order', 'sneaker', 'size']

