from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    response = redirect('/login/')
    return response
