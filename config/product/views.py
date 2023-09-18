from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Product
# Create your views here.


class Indicators(TemplateView):
    template_name = 'indicators.html'


class ProductsView(ListView):
    model = Product
    template_name = 'products.html'


class SaledProduct(TemplateView):
    template_name = 'sales.html'


# class
