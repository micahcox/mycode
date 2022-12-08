#!/usr/bin/python3

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# This view will return a 404 response
def ierror(request):
    return HttpResponseNotFound("Page was not found")
    
def success(request):
    return HttpResponse("Page was found")
