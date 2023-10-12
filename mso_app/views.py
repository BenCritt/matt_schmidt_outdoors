from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "mso_app/index.html")
    # The user will see this referred to as "/home" rather than "/index"
    # Best practice is to have the homepage HTML file named index.html
    # User experience is improved by displaying "/home" instead of "/index"


def about(request):
    return render(request, "mso_app/about.html")


def events(request):
    return render(request, "mso_app/events.html")


def our_work(request):
    return render(request, "mso_app/our_work.html")


def base(request):
    return render(request, "mso_app/base.html")
