from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpateForm
from django.contrib.auth.decorators import login_required


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
def confirm(request):
    return render(request, 'user/confirm.html')


# -------------- forgot pwd page ----------------
def forgot_password(request):
    return render(request, 'user/forgot_password.html')


# provide a code to the user on clicking the update item button

