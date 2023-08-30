from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'register'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('registers/', views.register, name='register'),
    
]
