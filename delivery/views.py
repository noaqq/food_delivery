# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

# from .forms import NewUserForm


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


# def register_user(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("delivery/start.html")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="delivery/register.html", context={"register_form":form})