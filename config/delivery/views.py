from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class PurchaseView(TemplateView):
    template_name = 'providers_order.html'


class PaymentsView(TemplateView):
    template_name = 'payments.html'
