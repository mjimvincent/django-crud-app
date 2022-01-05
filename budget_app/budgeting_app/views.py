from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django import template
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.template.loader import render_to_string
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
    users = User.objects.all()
    return render(request, "budgeting_app/users.html", {"users" : users})

@login_required(login_url="/login/")
def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            users = User.objects.all()
            data['html_user_list'] = render_to_string('includes/partial_user_list.html', {
                'users': users
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required(login_url="/login/")
def user_create(request):
    # context = {}
    # msg = None
    # success = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get("username")
        #     raw_password = form.cleaned_data.get("password1")
        #     user = authenticate(username=username, password=raw_password)

        #     msg = 'User created - please <a href="/login">login</a>.'
        #     success = True

        # #     return redirect("/login/")

        # else:
        # #     msg = 'Form is not valid'
        #     msg = form.errors
        #     #test user password: adminpassword123
    else:
        form = SignUpForm()

    # context["form"] = form
    # context["msg"] = msg
    # context["success"] = success

    return save_user_form(request, form, 'includes/partial_user_create.html')

@login_required(login_url="/login/")
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=user)
    else:
        form = SignUpForm(instance=user)
    return save_user_form(request, form, 'includes/partial_user_update.html')

@login_required(login_url="/login/")
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        users = User.objects.all()
        data['html_user_list'] = render_to_string('includes/partial_user_list.html', {
            'users': users
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('includes/partial_user_delete.html', context, request=request)
    return JsonResponse(data)

# @login_required(login_url="/login/")
# def users(request):
#     context = {'segment': 'users'}
#     users = User.objects.all()
#     context = {"users" : users}

#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'User created - please <a href="/login">login</a>.'
#             success = True

#         #     return redirect("/login/")

#         else:
#         #     msg = 'Form is not valid'
#             msg = form.errors
#             #test user password: adminpassword123
#     else:
#         form = SignUpForm()

#     context["form"] = form
#     context["msg"] = msg

#     return render(request, "budgeting_app/users.html", context)