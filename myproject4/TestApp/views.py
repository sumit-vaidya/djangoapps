from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    str2='''
    <html>
        <body bgcolor="red" text="yellow">
            <h1>Welcome to Django World</h1>
        </body>
    </html>
    '''
    return HttpResponse(str2)