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
            u = form.save()
            try:
                group = Group.objects.get(name="default_user")
                group.user_set.add(u)
            except Exception as er:
                # raise
                print(er)
            print("OK")
            authenticate(u)
            message = "Successfully !"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect("/")
        else:
            message = "Error !"
            messages.add_message(request, messages.ERROR, message)
            return render(request, "auth/register.html", {"form": form})

    return render(request, "auth/register.html", {"form": form})




class Employee(TemplateView):
    template_name ='contragents.html'