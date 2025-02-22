from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime
def input(request):
    date=datetime.datetime.now()
    return HttpResponse("<html><body bgcolor='red' text='yellow'> <h1>CURRENT DATE :"+str(date)+"</h1></body></html>")
