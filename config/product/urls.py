from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('', views.Indicators.as_view(), name='indicators'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
]
