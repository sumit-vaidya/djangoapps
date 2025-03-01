from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def input(request):
    str1="""
        <html>
            <body bgcolor="red" text="yellow">
                <h1>Welcome to PYTHON world</h1>
            </body>
        <html>
    """
    return HttpResponse(str1)
