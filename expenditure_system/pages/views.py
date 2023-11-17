from django.shortcuts import render

from django.views.generic import TemplateView  # Import TemplateView
# Create your views here.


class WelcomePageView(TemplateView):
    template_name = "welcome.html"


class UpdatePageView(TemplateView):
    template_name = "update.html"


class RegisterPageView(TemplateView):
    template_name = "register.html"


class ProfilePageView(TemplateView):
    template_name = "profile.html"


class LoginPageView(TemplateView):
    template_name = "login.html"


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"


class ConfirmPageView(TemplateView):
    template_name = "confirm.html"



# ___________________________________________ shanita ______________________________
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string

def login(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')

        # Generate a random token
        token = get_random_string(length=8)
        
        # Store the token in the session for verification later
        request.session['sent_token'] = token

        # Send the token to the user's email (add your email sending logic here)

        return redirect('confirm_page')  # Redirect to the confirmation page after sending the token

    return render(request, 'login.html')

def confirm_email(request):
    if request.method == 'POST':
        entered_token = request.POST.get('token_input')
        sent_token = request.session.get('sent_token')

        if entered_token == sent_token:
            messages.success(request, 'Email confirmed successfully!')
            # Redirect to the dashboard upon successful email confirmation
            return redirect('dashboard')  # Replace 'dashboard' with your dashboard page URL name
        else:
            messages.error(request, 'Invalid token. Please try again.')
            return redirect('confirm_page')

    return render(request, 'confirm.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def welcome(request):
    # Your logic here, if any
    return render(request, 'welcome.html')  # Rendering the welcome.html template

#________________________________________________ends here____________________