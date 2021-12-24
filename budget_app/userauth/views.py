from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        response = redirect('/dashboard/')
    else:
        response = redirect('/login/')
    
    return response
