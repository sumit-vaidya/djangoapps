from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'base.html')

def compute(request):
    name=request.GET['t1']
    rollno=request.GET['t2']
    branch = request.GET['t3']
    college = request.GET['t4']
    maths = int(request.GET['t5'])
    physics = int(request.GET['t6'])
    chemistry = int(request.GET['t7'])
    total=maths+physics+chemistry
    avg=total/3
    return HttpResponse("<html><body bgcolor='yellow' text='red'><h2>STUDENT NAME:"+name+
                        "<br>STUDENT ROLLNO:"+str(rollno)+
                        "<br>STUDENT BRANCH:" + branch +
                        "<br>STUDENT COLLEGE:" + college +
                        "<br>MATHS:" + str(maths) +
                        "<br>PHYSICS:" + str(physics) +
                        "<br>CHEMISTRY:" + str(chemistry) +
                        "<br>TOTAL MARKS:" + str(total) +
                        "<br>AVERAGE:" + str(avg) +"</h2></body></html>")