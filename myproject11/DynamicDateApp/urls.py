from django.urls import re_path
from DynamicDateApp import views

urlpatterns = [
    re_path(r'^$', views.input)
]