from django.utils.crypto import get_random_string
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render

from django.views.generic import TemplateView  # Import TemplateView
# Create your views here.


class WelcomePageView(TemplateView):
    template_name = "welcome.html"

    #  we can remove this in the future and see how it works
    def get(self, request):
        return render(request, 'welcome.html')


class UpdatePageView(TemplateView):
    template_name = "update.html"


class RegisterPageView(TemplateView):
    template_name = "register.html"

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("The username is ", username)
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
        print('I am here now')

        return render(request, self.template_name, {'form': form})


class ProfilePageView(TemplateView):
    template_name = "profile.html"


class LoginPageView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # this is supposed to change i.e either to get the username or email
        # user_email = request.POST.get('user_email')
        username = request.POST.get('username')
        # print("The captured username is ", username)

        # Generate a random token
        token = get_random_string(length=8)

        # Store the token in the session for verification later
        request.session['sent_token'] = token

        # Send the token to the user's email (add your email sending logic here)

        # Redirect to the confirmation page after sending the token
        return redirect('confirm_page')


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request):
        return render(request, 'dashboard.html')


class ConfirmPageView(TemplateView):
    template_name = "confirm.html"


class StaffPageView(TemplateView):
    template_name = "staff.html"


class AddPageView(TemplateView):
    template_name = "add.html"


class QuantityPageView(TemplateView):
    template_name = "quantity.html"


class ItemPageView(TemplateView):
    template_name = "item.html"


# ___________________________________________ shanita ______________________________
# views.py


# def login(request):
#     if request.method == 'POST':
#         user_email = request.POST.get('user_email')

#         # Generate a random token
#         token = get_random_string(length=8)

#         # Store the token in the session for verification later
#         request.session['sent_token'] = token

#         # Send the token to the user's email (add your email sending logic here)

#         # Redirect to the confirmation page after sending the token
#         return redirect('confirm_page')

#     return render(request, 'login.html')


def confirm_email(request):
    if request.method == 'POST':
        entered_token = request.POST.get('token_input')
        sent_token = request.session.get('sent_token')

        if entered_token == sent_token:
            messages.success(request, 'Email confirmed successfully!')
            # Redirect to the dashboard upon successful email confirmation
            # Replace 'dashboard' with your dashboard page URL name
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid token. Please try again.')
            return redirect('confirm_page')

    return render(request, 'confirm.html')


# def dashboard(request):
#     return render(request, 'dashboard.html')


# def welcome(request):
#     # Your logic here, if any
#     # Rendering the welcome.html template
#     return render(request, 'welcome.html')

# ________________________________________________ends here____________________
