from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    str1='''
    <html>
        <body bgcolor="yellow" text="red">
            <h1>Welcome to Python World</h1>
        </body>
    </html>
    '''
    return HttpResponse(str1)