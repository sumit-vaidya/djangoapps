from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=int(dt.strftime("%H"))
    msg = "Hello Hyderabad....."
    if hour<=12:
        msg += "Very Good Morning!!!"
    elif hour<=16:
        msg += "Very Good Afternoon!!!"
    elif hour<=20:
        msg += "Very Good Evening!!!"
    else:
        msg += "Very Good Night!!!"
    dict1={'date': dt, 'msg': msg}
    return render(request, 'base.html', dict1)