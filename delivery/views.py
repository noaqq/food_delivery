from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import RegisterUserForm


def anonymous_required(function=None, redirect_url="start"):

    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous, login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def start(request):
    return render(request, "delivery/start.html" ) 


def about(request):
    return render(request, "delivery/about.html")


@login_required(login_url="/")
def menu(request):
    return render(request, "delivery/menu.html")


def faq(request):
    return render(request, "delivery/faq.html")


@login_required(login_url="start")
def delivery(request):
    return render(request, "delivery/delivery.html")


@anonymous_required
def regist(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("start")
    else:
        form = RegisterUserForm()
    return render(request, "delivery/regist.html", {"form":form})


@anonymous_required
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("start")
        else:
            messages.success(request, "Логин или пароль неверны")
            return render(request, "delivery/login_user.html")
    else:
        return render(request, "delivery/login_user.html")


@login_required(login_url="start")
def logout_user(request):
    logout(request)
    return redirect("start")