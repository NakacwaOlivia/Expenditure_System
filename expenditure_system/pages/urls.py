from django.urls import path
from .views import WelcomePageView, UpdatePageView, RegisterPageView, ProfilePageView, LoginPageView, DashboardPageView, ConfirmPageView

urlpatterns = [
    path('', WelcomePageView.as_view(), name='welcome'),
    path('update/', UpdatePageView.as_view(), name='update'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('confirm/', ConfirmPageView.as_view(), name='confirm'),

]