from django.urls import path, re_path

from . import views
from django.conf.urls import url

##ORIG
# urlpatterns = [
#     path("dashboard/", views.dashboard, name="dashboard"),
# ]

##C + P
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Users page
    path('users/', views.users, name='users'),

    url(r'^create/$', views.user_create, name='user_create'),
    url(r'^users/(?P<pk>\d+)/update/$', views.user_update, name='user_update'),
    url(r'^users/(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    re_path(r'^.*\.html', views.pages, name='pages'),
    # path(r'.*\.*', views.pages, name='pages'),

]

