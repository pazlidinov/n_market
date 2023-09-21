from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import DeliveredItem, DeliveringCompany
# Create your views here.


class PurchaseView(ListView):
    model = DeliveredItem
    template_name = 'providers_order.html'


class PaymentsView(TemplateView):
    template_name = 'payments.html'
