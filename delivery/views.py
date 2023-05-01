from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from delivery.models import Basket, Catalog

from .forms import CatalogForm, RegisterUserForm


def anonymous_required(function=None, redirect_url="start"):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(lambda u: u.is_anonymous, login_url=redirect_url)

    if function:
        return actual_decorator(function)
    return actual_decorator


def start(request):
    return render(request, "delivery/start.html")


def create(request):
    submitted = False
    if request.method == "POST":
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create?submitted=True")
    else:
        form = CatalogForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "delivery/create.html", {"form": form, "submitted": submitted})


# def search_food(request):
#     if request.method == "GET":
#         error = None
#         Catalog_food = Catalog.objects.filter(name = request.GET["food"])
#         if not Catalog:
#             error = "No food"
#         return render(request, "delivery/search.html", {"Catalog_food": Catalog_food, "error": error})


@login_required(login_url="/")
def menu(request):
    if request.method == "POST":
        user = request.POST["user"]
        name = request.POST["name"]
        price = request.POST["price"]
        image = request.POST["image"]
        sale = Basket.objects.create(user=user, name=name, price=price, image=image)
        sale.save()
        print(user, name, price, image)
        messages.success(request, ("Товар успещно добавлен в корзину."))
        return redirect("menu")
    food_list = Catalog.objects.order_by("name")
    return render(request, "delivery/menu.html", {"food_list": food_list})


def faq(request):
    return render(request, "delivery/faq.html")


def order(request):
    return render(request, "delivery/order.html")


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
    return render(request, "delivery/regist.html", {"form": form})


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

    # def basket(request):
    #     if request.method == "POST":
    #         user = request.POST["user"]
    #         name = request.POST["name"]
    #         order = Basket.objects.create(user=user, name=name)
    #         order.save()
    #         print(user, name)
    #         messages.success(request, ("Товар успещно добавлен в корзину."))
    #         return render(request, "delivery/order.html")

    # def basket(request):
    # food_list = Basket.objects.all()

    # sum = Basket.objects.aggregate(Sum('price'))['price__sum']
    # total = sum + 99
    # return render(request, "delivery/order.html", {"food_list": food_list, "sum": sum, "total": total})


def basket(request):
    basket_items = Basket.objects.filter(user=request.user)
    sum_price = basket_items.aggregate(Sum('price'))['price__sum']
    total = sum_price + 99

    if request.method == 'POST':
        print(request.POST)
        item_id = request.POST.get('item_id')
        item_to_delete = Basket.objects.get(id=item_id)
        item_to_delete.delete()
        print('Item deleted:', item_id)
        return redirect('order')

    context = {
        "food_list": basket_items,
        "sum_price": sum_price,
        "total": total,
    }

    return render(request, 'delivery/order.html', context)


def payment(request):
    return render(request, 'delivery/payment.html')
