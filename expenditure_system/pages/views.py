from django.utils.crypto import get_random_string
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.shortcuts import render
# from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
import random, string
from django.views import View
from .forms import RegisterForm



from django.views.generic import TemplateView  # Import TemplateView
# Create your views here.


class WelcomePageView(TemplateView):
    template_name = "welcome.html"

    #  we can remove this in the future and see how it works
    def get(self, request):
        return render(request, 'welcome.html')


class UpdatePageView(TemplateView):
    template_name = "update.html"


# class RegisterPageView(TemplateView):
#     template_name = "register.html"

#     def get(self, request):
#         form = UserRegisterForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             print("The username is ", username)
#             messages.success(request, f'Account created for {username}!')

#             return redirect('login')

#         return render(request, self.template_name, {'form': form})

class RegisterPageView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='dashboard')

        # else process dispatch as it otherwise normally would
        return super(RegisterPageView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class ProfilePageView(TemplateView):
    template_name = "profile.html"


class LoginPageView(TemplateView):
    template_name = "login.html"

    # def get(self, request):
    #     return render(request, 'login.html')

    # def post(self, request):
    #     # this is supposed to change i.e either to get the username or email
    #     # user_email = request.POST.get('user_email')
    #     username = request.POST.get('username')
    #     # print("The captured username is ", username)

    #     # Generate a random token
    #     token = get_random_string(length=8)

    #     # Store the token in the session for verification later
    #     request.session['sent_token'] = token

    #     # Send the token to the user's email (add your email sending logic here)

    #     # Redirect to the confirmation page after sending the token
    #     return redirect('confirm_page')

class ForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'forgot_password.html'

    # email_template_name = 'users/password_reset_email.html'
    # subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')


    
# _________________________ samuel _________________________
class DashboardPageView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request):
        return render(request, 'dashboard.html')


class LogoutPageView(TemplateView):
    template_name = 'logout.html'
    
    def get(self, request):
        return render(request, 'logout.html')


class StaffPageView(TemplateView):
    template_name = "dashboard/staff.html"


class QuantityPageView(TemplateView):
    template_name = "dashboard/quantity.html"


class ItemPageView(TemplateView):
    template_name = "dashboard/item.html"

# _________________________ end of samuel _________________________



class ConfirmPageView(TemplateView):
    template_name = "confirm.html"


# ___________________________________________ shanita ______________________________
# views.py

def confirm_email(request):
    if request.method == 'POST':
        entered_token = request.POST.get('token_input')
        sent_token = request.session.get('sent_token')

        if entered_token == sent_token:
            # If the entered token matches the sent token
            messages.success(request, 'Email confirmed successfully!')
            # Redirect to the dashboard upon successful email confirmation
            return redirect('dashboard')  # Replace 'dashboard' with your dashboard page URL name
        else:
            # If the tokens do not match, display an error message
            messages.error(request, 'Invalid token. Please try again.')
            return redirect('confirm_page')

    return render(request, 'confirm.html')

def dashboard(request):
    if not request.session.get('email_confirmed'):
        # If the email is not confirmed, redirect to the confirmation page
        messages.info(request, 'Please confirm your email to access the dashboard.')
        return redirect('confirm_page')  # Redirect to the confirmation page URL

    # If the email is confirmed, render the dashboard
    return render(request, 'dashboard.html')


def validate_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('securitycode')
        # Perform the validation logic
        if entered_code == '123456':  # Replace 'your_secret_code' with the actual secret code
            messages.success(request, 'Code verified successfully!')
            return redirect('update')
        else:
            # if the code is invalid, display an error message
            error_message = 'Invalid code. Please try again.'
            messages.error(request, error_message)
            return redirect('dashboard')
    return redirect('dashboard')  # Redirect to the home page if the form is not submitted


