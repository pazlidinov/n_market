from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            authenticate(u)
            login(request, u)
            return redirect("/")
        else:
            return render(request, "auth/register.html", {"form": form})

    return render(request, "auth/register.html", {"form": form})
