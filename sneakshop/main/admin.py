from django.contrib import admin
from . import models

@admin.register(models.Sneaker)
class AdminSneaker(admin.ModelAdmin):
    list_display = ['brand', 'name', 'slug', 'category', 'color', 'available', 'image', 'description', 'price', 'created']
    prepopulated_fields = {'slug': ('brand', 'name')}

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Color)
class AdminColor(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(models.Size)
class AdminSneaker(admin.ModelAdmin):
    list_display = ['size']

@admin.register(models.SneakerSize)
class AdminSneakerSize(admin.ModelAdmin):
    list_display = ['sneaker', 'size', 'available', 'amount']


