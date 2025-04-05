from django.shortcuts import render
from ModelApp.models import Emp # from .models import Emp

# Create your views here.
def input(request):
    emps = Emp.objects.all()
    return render(request, 'base.html', {'emps':emps})