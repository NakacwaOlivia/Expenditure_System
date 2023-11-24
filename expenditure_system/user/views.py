from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .utils import send_otp
from datetime import datetime       
import pyotp
from django.contrib.auth.models import User

#-------------Login-------------------
def login(request):
    error_message = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            send_otp(request)
            request.session['username'] = username
            return redirect('confirm')
        else:
            error_messsage = "Username or Password is incorrect"
    return render(request, 'user/login.html', {'error_messsage': error_messsage})



# -----------------------Confirm-------------------------
def confirm(request):
    error_message = None
    if request.method == 'POST':

        token_input = request.POST['token_input']   
        username = request.session['username']

        token_secret_key = request.session['token_secret_key']
        token_input_valid_date = request.session['token_input_valid_date']
        

        if token_secret_key and token_input_valid_date is not None:
            valid_date = datetime.fromisoformat(token_input_valid_date)

            if valid_date > datetime.now():
                token = pyotp.TOTP(token_secret_key, interval=60)
                
                if token.verify(token_input):
                    user = get_object_or_404(User, username=username)
                    login(request, user)

                    del request.session['token_secret_key']
                    del request.session['token_input_valid_date']

                    return redirect('dashboard')
                else:
                    error_message = 'Invalid OTP'

    return render(request, 'user/confirm.html', {'username': request.session.get('username', None), 'error_message': error_message})

    # return render(request, 'user/confirm.html', {'username': request.session['username']})


# @login_required(login_url='user-login')
# def dashboard(request):
#     return render(request, 'user/dashboard.html', {'username': request.session['username']})



def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')

    else:
        form = CreateUserForm()
    context = {
        'form': form,
               }
    return render(request, 'user/register.html', context)

def welcome(request):
    return render(request, 'welcome.html')


def profile(request):
    return render(request, 'user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpateForm(request.POST, request.FILES, instance=request.user.profile)
    
    else: 
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpateForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profiel_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)



# -------------- confirm page ----------------
def forgot_password(request):
    return render(request, 'user/forgot_password.html')



