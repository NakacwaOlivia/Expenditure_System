from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/details/<int:pk>/', views.staff_details, name='dashboard-staff-details'),
    path('item/', views.item, name='dashboard-item'),
    path('register/', user_views.register, name='user-register'),
    path('', views.welcome, name='welcome'), 
<<<<<<< HEAD
    path('update/', views.update, name='update'),  
=======
    path('update/', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('item/update/<int:pk>/', views.item_update, name='dashboard-item-update'),
    path('item/delete/<int:pk>/', views.item_delete, name='dashboard-item-delete'),
>>>>>>> 68de7b09f24e1239b6f20f2d667a52d61cb056a5
      
]
