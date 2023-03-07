from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("start")
    else:
        form = RegisterForm()
    return render(request, "delivery/regist.html", {"form":form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("start")
        else:
            messages.success(request, "Логин или пароль неверны")
            return render(request, "delivery/login_user.html")
    else:
        return render(request, "delivery/login_user.html")


def logout_user(request):
    logout(request)
    return redirect("start")