from django.shortcuts import render, redirect, get_object_or_404
from .models import Sneaker, Category, SneakerSize

def index(request):
    return render(
        request,
        'main/index.html',
    )
    

# def catalog(request):
#     sneakers = Sneaker.objects.filter(available = True)
#     return render(
#         request,
#         'main/catalog.html',
#         {
#             'sneakers': sneakers
#         }
#     )

def catalog(request, category_slug = None):
    sneakers = Sneaker.objects.filter(available = True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        sneakers = Sneaker.objects.filter(category = category)
    return render(
        request,
        'main/catalog.html',
        {
            'category': category,
            'sneakers': sneakers
        }
    )

def product_details(request, slug):
    sneaker = get_object_or_404(Sneaker, slug = slug, available = True) 
    sizes = SneakerSize.objects.filter(sneaker=sneaker, available = True)
    return render(
        request,
        'main/detail.html',
        {
            'sneaker': sneaker,
            'sizes': sizes
        }
    )
    
