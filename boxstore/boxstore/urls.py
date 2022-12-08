#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('ierror/', views.ierror),
    path('success/', views.success),
]
