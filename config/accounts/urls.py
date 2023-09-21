from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name="auth/logout.html"), name="logout"),

    path('register/', views.register, name='register'),
    
    
    path('employee/', views.employee, name='employee'),
    path('kontragent_form/', views.KontragentFormView.as_view(), name='kontragents'),
    
]
