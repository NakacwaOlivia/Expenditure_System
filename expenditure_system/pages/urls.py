from django.urls import path
from .views import WelcomePageView, UpdatePageView, RegisterPageView, ProfilePageView, LoginPageView, DashboardPageView, ConfirmPageView, StaffPageView, QuantityPageView, ItemPageView, LogoutPageView
# urls.py

# _____________________edited this to new one_______________
from django.urls import path
from . import views
from .views import validate_code

# ________________________original code___________________
urlpatterns = [
    path('', WelcomePageView.as_view(), name='welcome'),
    path('update/', UpdatePageView.as_view(), name='update'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('confirm/', ConfirmPageView.as_view(), name='confirm'),
    path('staff/', StaffPageView.as_view(), name='staff'),
    path('quantity/', QuantityPageView.as_view(), name='quantity'),
    path('item/', ItemPageView.as_view(), name='item'),
    path('validate-code/', validate_code, name='validate_code'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    

]
