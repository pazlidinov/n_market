from django.urls import path
from . import views


app_name = 'delivery'

urlpatterns = [

    path('payments/', views.PaymentsView.as_view(), name='payments'),
]
