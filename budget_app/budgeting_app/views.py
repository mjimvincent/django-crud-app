from django.shortcuts import render

from django.http import HttpResponse


def dashboard(response):
    return render(response, "admin/index.html", {})
