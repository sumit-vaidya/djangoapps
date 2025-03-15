from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=int(dt.strftime("%H"))
    if hour<=12:
        return render(request, 'morning.html', {'date': dt})
    elif hour<=16:
        return render(request, 'afternoon.html', {'date': dt})
    elif hour<=20:
        return render(request, 'evening.html', {'date': dt})
    else:
        return render(request, 'night.html', {'date': dt})