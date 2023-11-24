from django.shortcuts import render
from django.http import HttpResponse
# from .models import Staff, Item, Quantity
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    return render(request, 'dashboard/index.html')


def staff(request):
    return render(request, 'dashboard/staff.html')


def item(request):
    return render(request, 'dashboard/item.html')


def quantity(request):
    return render(request, 'dashboard/quantity.html')


def update(request):
    return render(request, 'update.html')
