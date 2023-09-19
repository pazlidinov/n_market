from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from .forms import UserRegisterForm




def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                group = Group.objects.get(name="Default User")
                group.user_set.add(user)
            except Exception as er:
                print(er)
            authenticate(user)
            login(request, user)
        return redirect('/accounts/login')
    return render(request, "auth/register.html", {"form": form})


class Employee(TemplateView):
    template_name ='contragents.html'