from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('home/', views.Home, name="Home"),
    path('profile/<int:pk>/', views.profilePage, name="profilePage"),
    path('index/', views.index),
    path('navbar/', views.NavBar),
    path('audio/', views.Audio),
    path('footer/', views.Footer),
    path ('cart/', views.Cart),
    path('createCustomer/', views.createCustomer, name="createCustomer"),
    path('update_customer/<int:pk>/', views.updateCustomer, name="updateCustomer"),
    path('delete_customer/<int:pk>/', views.deleteCustomer, name="deleteCustomer"),
        ]