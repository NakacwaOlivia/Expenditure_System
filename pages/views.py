from django.shortcuts import render
from django.contrib.auth import authenticate, login

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

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, '/templates/dashboard.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'templates/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'templates/login.html')