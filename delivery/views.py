from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm


def start(request):
    return render(request, "delivery/start.html" ) 


def about(request):
    return render(request, "delivery/about.html")


def menu(request):
    return render(request, "delivery/menu.html")


def faq(request):
    return render(request, "delivery/faq.html")


def delivery(request):
    return render(request, "delivery/delivery.html")


def regist(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "delivery/regist.html", {"form":form})

def login(request):
    return render(request, "delivery/login_user.html")