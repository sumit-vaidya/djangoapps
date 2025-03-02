from django.urls import re_path
from AddApp import views

urlpatterns = [
    re_path(r'^$',views.input),
    re_path(r'^add$',views.add)
]
