from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # try:
            #     group = Group.objects.get(name="user")
            #     group.user_set.add(u)
            # except Exception as er:
            #     authenticate(u)
            authenticate(user)
            return redirect("/accounts/login/")
        else:
            return render(request, "auth/register.html", {"form": form})

    return render(request, "auth/register.html", {"form": form})


class Employee(TemplateView):
    template_name ='contragents.html'