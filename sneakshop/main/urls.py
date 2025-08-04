from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.product_details, name='detail'),
]
