from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.views import generic


def register(request):
    form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # add user to group
            gp = Group.objects.get(name="users")
            user.groups.add(gp.id)
            user.save()
            # login new user
            login(request, user)
            return redirect("/")
        else:
            form = UserCreationForm()
    else:

        return render(request, "auth/register.html", {"form": form})
    return render(request, "auth/register.html", {"form": form})
