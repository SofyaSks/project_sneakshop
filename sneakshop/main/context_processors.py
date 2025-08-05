from .models import Category

def base_context(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }