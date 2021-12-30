from django.urls import path, re_path

from . import views

##ORIG
# urlpatterns = [
#     path("dashboard/", views.dashboard, name="dashboard"),
# ]

##C + P
urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    re_path(r'^.*\.html', views.pages, name='pages'),
    # path(r'.*\.*', views.pages, name='pages'),

]

