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