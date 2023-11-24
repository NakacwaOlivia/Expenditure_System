from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm
from django.core.mail import send_mail
from .token import generated_access_code
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

def welcome(request):
    # make the user code global
    return render(request, 'welcome.html')

@login_required
# @login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    workers = User.objects.all()
    
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_details(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_details.html', context)

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

@login_required
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

# function to send an email to a user:: call the func and pass the email_to and token/code
def sendEmail(secret_code):
    subject = 'Add Item: Verification Code'
    message = f'Hi, We have noticed urge to update items. Your access code is {secret_code}.'
    email_from = settings.EMAIL_HOST_USER
    email_to = 'mugizi@duck.com'
    recipient_list = [email_to, ]

    send_mail(subject, message, email_from, recipient_list)
    # print('Email has been sent successfully to mugizi@duck.com')

@login_required
def validate_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('securitycode')
        user_code = generated_access_code()
        sendEmail(user_code)
        # Perform the validation logic
        if entered_code == user_code: 
            messages.success(request, 'Code verified successfully!')
            return redirect('add')
        else:
            # if the code is invalid, display an error message
            error_message = 'Invalid code. Please try again.'
            messages.error(request, error_message)
            return redirect('dashboard-index')
    return redirect('dashboard-index')  # Redirect to the home page if the form is not submitted


@login_required
# function to generate a random code
def generateCode(request):
    # Generate a random code
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print("The generated code to be sent is ", code)
    return HttpResponse(status=200)