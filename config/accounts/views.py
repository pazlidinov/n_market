from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm







def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Successfully Created for {username} Login In Now!!!')
            return redirect('accounts/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})



class Employee(TemplateView):
    template_name ='contragents.html'