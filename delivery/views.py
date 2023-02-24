# from django.http import HttpResponse
from django.shortcuts import render


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

