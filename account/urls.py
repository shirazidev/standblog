from django.urls import path
from . import views
from django.shortcuts import redirect
urlpatterns = [
    path('login', views.user_login),
    path('register', views.user_register),
    path('logout', views.user_logout, name='logout'),
]
