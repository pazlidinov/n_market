from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from .forms import UserRegisterForm
from django.core.paginator import Paginator
from .models import User






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




def employee(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    object_list = User.objects.filter(is_staff=True).page_obj = paginator.get_page(page_number)

    
    context = {
        'object_list':object_list,
        
    }
    
   
    return render(request, 'contragents.html', context)



class KontragentFormView(CreateView):
    model = User
    template_name = 'forms/contragent_form.html'
    fields = ['password', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'email', 'status', 'birthday', 'age', 'phone', 'address']
    success_url = '/'
   