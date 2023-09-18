from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class Indicators(TemplateView):
    template_name = 'indicators.html'


class ProductsView(TemplateView):
    template_name = 'products.html'
    
class SaledProduct(TemplateView):
    template_name = 'sales.html'
    
    
# class 