from django.urls import re_path
from GreetingApp import views, views1

urlpatterns = [
    #re_path(r'^$', views.input),
    re_path(r'^$', views1.input)
]