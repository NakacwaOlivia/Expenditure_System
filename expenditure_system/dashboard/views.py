from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm


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
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'dashboard/item.html', context)


@login_required
def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-item')
    return render(request, 'dashboard/item_delete.html')


def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-item')
    else:
        form = ItemForm(instance=item)
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/item_update.html', context)

@login_required
def update(request):
    return render(request, 'update.html')


@login_required
def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-item')
    else:
        form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add.html', context)