from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    date=datetime.datetime.now()
    hour=int(date.strftime('%H'))
    msg = "Hello Hyderabad!"
    msg2= "The Current Date and Time is : {}"
    if hour<=12:
        msg=msg+"Very Good Morning!!"+msg2.format(str(date))
    elif hour<=16:
        msg=msg+"Very Good Afternoon!!"+msg2.format(str(date))
    elif hour<=20:
        msg=msg+"Very Good Evening!!"+msg2.format(str(date))
    else:
        msg=msg+"Very Good Night!!"+msg2.format(str(date))
    dict={'msg':msg,'date':date}
    return render(request,'base.html',dict)