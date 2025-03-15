from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import datetime
def input(request):
    dt=datetime.datetime.now()
    day=dt.strftime("%A")
    month=dt.strftime("%B")
    year=dt.strftime("%Y")
    dict1={'date': dt, 'cur_day': day, 'cur_month': month, 'cur_year': year}
    return render(request, 'base.html', dict1)