from django.urls import path
from . import views


app_name = 'delivery'

urlpatterns = [
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('payments/', views.PaymentsView.as_view(), name='payments'),
]
