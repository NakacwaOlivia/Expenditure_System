from django.shortcuts import render
from django.http import HttpResponse
# from .models import Staff, Item, Quantity
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')

@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def item(request):
    return render(request, 'dashboard/item.html')


@login_required
def quantity(request):
    return render(request, 'dashboard/quantity.html')

@login_required
def update(request):
    return render(request, 'update.html')
