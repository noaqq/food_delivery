from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

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


def update(request):
    submitted = False
    if request.method == "POST":
        product_id = request.POST.get('product')
        product = Catalog.objects.get(id=product_id)
        form = CatalogForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/update?submitted=True")
    else:
        form = CatalogForm
        if "submitted" in request.GET:
            submitted = True
    products = Catalog.objects.all()
    return render(request, "delivery/update.html", {"form": form, "products": products, "submitted": submitted})


def delete(request, id):
    catalog = get_object_or_404(Catalog, id=id)
    catalog.delete()
    return HttpResponseRedirect("/create")


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


def menu_category(request, category):
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
    food_list = Catalog.objects.filter(category=category).order_by("name")
    return render(request, "delivery/menu.html", {"food_list": food_list})


def faq(request):
    return render(request, "delivery/faq.html")


def order(request):
    return render(request, "delivery/order.html")


@login_required(login_url="start")
def delivery(request):
    return render(request, "delivery/delivery.html")


def regist(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = User.objects.create_user(
                username=request.POST["username"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password1"],
            )
            user.save()
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


def basket(request):
    basket_items = Basket.objects.filter(user=request.user)
    sum_price = basket_items.aggregate(Sum('price'))['price__sum']
    total = 0
    if sum_price is None:
        sum_price = 0
    else:
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


def sort_food(request):
    if request.method == 'POST':
        if request.POST.get("sort_option") == 'highest_price':
            food_list = Catalog.objects.order_by("price").reverse()
            context = {
                "food_list": food_list,
            }
        else:
            food_list = Catalog.objects.order_by("price")
            context = {
                "food_list": food_list,
            }
    return render(request, 'delivery/menu.html', context)


def clear_basket(request):
    Basket.objects.filter(user=request.user).delete()
    return render(request, "delivery/order.html")


def payment(request):
    return render(request, 'delivery/payment.html')
