from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    str1="""
        <html>
            <body bgcolor="red" text="yellow">
                <h1>Hello! Good Morning</h1>
            </body>
        <html>
    """
    return HttpResponse(str1)