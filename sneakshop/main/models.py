from django.db import models
from django.urls import reverse 

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Category')
    slug = models.SlugField(max_length=20)

    class Meta:
        # verbose_name = 'Категория'
        # verbose_name_plural = 'Категории'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog_by_category', args = [self.slug])
    
class Color(models.Model):
    name = models.CharField(max_length=20, unique= True, verbose_name='Color')
    slug = models.SlugField(max_length=20)

    # class Meta:
    #     verbose_name = 'Цвет'
    #     verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name
    

class Size(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1, unique=True)

    # class Meta:
    #     verbose_name = 'Размер'
    #     verbose_name_plural = 'Размеры'

    def __str__(self):
        return str(self.size)


class Sneaker(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sneakers')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,related_name='sneakers') 
    available = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='images%Y%m%d')
    sizes = models.ManyToManyField(Size, through = 'SneakerSize',related_name='sneakers')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', args = [self.slug])

    def __str__(self):
        return self.name

class SneakerSize(models.Model):
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    available = models.BooleanField(default=True)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.size)

    # class Meta:
    #     verbose_name = 'Размер кроссовок'
    #     verbose_name_plural = 'Размеры кроссовок'



