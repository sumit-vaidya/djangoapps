from django.contrib import admin
from django.urls import re_path
#from SampleApp import views
from . import views    # we can use (.) because urls.py and view.py is in same folder

urlpatterns = [
    re_path(r'^sample$', views.display),
]