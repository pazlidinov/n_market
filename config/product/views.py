from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Product
# Create your views here.


class Indicators(TemplateView):
    template_name = 'indicators.html'


class ProductsView(ListView):
    model = Product
    template_name = 'products.html'


class SaledProduct(TemplateView):
    template_name = 'sales.html'


class AddForm(CreateView):
    model = Product
    template_name = 'forms/product_form.html'
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.all().select_related(
            'category', 'subcategory', 'brand', 'measure')
        print(context["product"])
        return context
