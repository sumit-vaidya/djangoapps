from django.contrib import admin
from django.urls import path,re_path
from TestApp import views as v1
from SampleApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^test$', v1.input),
    re_path(r'^sample$', v2.display)
]
