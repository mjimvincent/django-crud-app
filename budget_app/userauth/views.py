from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignUpForm
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
        # return HttpResponse("Hello")
        # return render(request, "accounts/login.html", {})
        form = LoginForm(request.POST or None)

        msg = None

        if request.method == "POST":

                if form.is_valid():
                        username = form.cleaned_data.get("username")
                        password = form.cleaned_data.get("password")
                        user = authenticate(username=username, password=password)
                        if user is not None:
                                login(request, user)
                                return redirect("/")
                        else:
                                msg = 'Invalid credentials'
                else:
                        msg = 'Error validating the form'

        return render(request, "userauth/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        #     return redirect("/login/")

        else:
        #     msg = 'Form is not valid'
            msg = form.errors
            #test user password: adminpassword123
    else:
        form = SignUpForm()

    return render(request, "userauth/register.html", {"form": form, "msg": msg, "success": success})
