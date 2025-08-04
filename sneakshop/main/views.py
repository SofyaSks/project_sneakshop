from django.shortcuts import render, redirect, get_object_or_404
from .models import Sneaker

def index(request):
    return render(
        request,
        'main/index.html'
    )

def catalog(request):
    sneakers = Sneaker.objects.filter(available = True)
    return render(
        request,
        'main/catalog.html',
        {
            'sneakers': sneakers
        }
    )

def product_details(request, slug):
    sneaker = get_object_or_404(Sneaker, slug = slug, available = True)
    return render(
        request,
        'main/detail.html',
        {
            'sneaker': sneaker
        }
    )
    
