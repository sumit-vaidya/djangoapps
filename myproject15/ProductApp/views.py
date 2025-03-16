from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'base.html')
def display(request):
    id = int(request.GET['t1'])
    name = request.GET['t2']
    price = int(request.GET['t3'])
    brand = request.GET['t4']
    qty= int(request.GET['t5'])
    dict1={'id':id, 'name':name, 'price':price, 'brand':brand, 'qty':qty}
    return render(request, 'base2.html', dict1)
