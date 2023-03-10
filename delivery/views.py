from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import RegisterUserForm, catalogForm
from .models import *


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


def create(request):
    submitted = False
    if request.method == "POST":
        form = catalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create?submitted=True")
    else:
        form = catalogForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "delivery/create.html", {"form": form, "submitted": submitted})


# def search_food(request):
#     if request.method == "GET":
#         error = None
#         catalog_food = catalog.objects.filter(name = request.GET["food"])
#         if not catalog:
#             error = "No food"
#         return render(request, "delivery/search.html", {"catalog_food": catalog_food, "error": error})



@login_required(login_url="/")
def menu(request):
    food_list = catalog.objects.all()
    return render(request, "delivery/menu.html", {"food_list":food_list})


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
            messages.success(request, "?????????? ?????? ???????????? ??????????????")
            return render(request, "delivery/login_user.html")
    else:
        return render(request, "delivery/login_user.html")


@login_required(login_url="start")
def logout_user(request):
    logout(request)
    return redirect("start")