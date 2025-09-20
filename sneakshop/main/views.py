from django.shortcuts import render, redirect, get_object_or_404
from .models import Sneaker, Category, SneakerSize
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from.forms import FilterSortForm


def catalog(request, category_slug = None):
    sneakers = Sneaker.objects.filter(available = True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        sneakers = Sneaker.objects.filter(category = category)

    form = FilterSortForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        cd = form.cleaned_data
        brand = cd['brand']
        color = cd['color']
        sort = cd['sort']
        if brand:
            sneakers = sneakers.filter(brand = brand)
        if color:
            sneakers = sneakers.filter(color=color)
        if sort == 'lth':
            sneakers = sneakers.order_by('price')
        if sort == 'htl':
            sneakers = sneakers.order_by('-price')



    return render(
        request,
        'main/catalog.html',
        {
            'category': category,
            'sneakers': sneakers,
            'form': form
        }
)




        

def product_details(request, slug):
    sneaker = get_object_or_404(Sneaker, slug = slug, available = True) 
    sizes = SneakerSize.objects.filter(sneaker=sneaker, available = True)
    cart_product_form = CartAddProductForm(sneaker = sneaker)
    return render(
        request,
        'main/detail.html',
        {
            'sneaker': sneaker,
            'sizes': sizes,
            'cart_product_form': cart_product_form,
        }
    )
    
def new(request):
    sneakers = Sneaker.objects.filter(available=True).order_by('-created')[:6]
    
    return render(
        request,
        'main/new.html',
        {
            'sneakers': sneakers
        }
    )

def contacts(request):
    return render(
        request,
        'main/contacts.html',

    )