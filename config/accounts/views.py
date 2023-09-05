from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group

from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            u = form.save()
            try:
                group = Group.objects.get(name="user")
                group.user_set.add(u)
            except Exception as er:
                # raise
                print(er)
            authenticate(u)
            return redirect("/accounts/login/")
        else:
            return render(request, "auth/register.html", {"form": form})
=======
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
>>>>>>> 0f7798c2563e720abd4a1e32cf8df7cf082d60e8

    return render(request, "auth/register.html", {"form": form})


