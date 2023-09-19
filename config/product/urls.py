from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('', views.Indicators.as_view(), name='indicators'),
   
    path('products/', views.ProductsView.as_view(), name='products'),
    
    path('sales/', views.SaledProduct.as_view(), name='sales'),
    
    path('add/', views.AddForm.as_view(), name='add'),
]
