from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django import template
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User

#This is for modal signup
from django.contrib.auth import authenticate
from userauth.forms import SignUpForm
#Modal

##Orig
# def dashboard(response):
#     return render(response, "budgeting_app/dashboard.html", {})

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    # html_template = loader.get_template('budgeting_app/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, "budgeting_app/index.html", context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try: 
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        html_template = loader.get_template('budgeting_app/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('budgeting_app/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('budgeting_app/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def users(request):
    context = {'segment': 'users'}
    users = User.objects.all()
    context = {"users" : users}

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

    context["form"] = form
    context["msg"] = msg

    return render(request, "budgeting_app/users.html", context)