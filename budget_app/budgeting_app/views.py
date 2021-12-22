from django.shortcuts import render

from django.http import HttpResponse


def dashboard(response):
    return render(response, "budgeting_app/dashboard.html", {})
