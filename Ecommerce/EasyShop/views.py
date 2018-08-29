from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from .models import Categories, Items, Users, Orders
from django.core import serializers
from django.db.models import Q,Sum,Count,Avg,Max
from .forms import Users_Form






def orders(request):
    ord= Orders.objects.all()
    if ord:
        context = {
            'ord': ord
        }
        return render(request, 'basic.html', context)
    else:
        return HttpResponseNotFound("no orders found")

def  items(request):
    item=Items.objects.all()
    if item:
        context = {
            'item' : item
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No items found here")

def  users(request):
    users=Users.objects.all()
    if users:
        context = {
            'users' : users
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No users found here")

def  categories(request):
    categorie=Categories.objects.all()
    if categorie:
        context = {
            'categorie' : categorie
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No categories found here")


def pricerange(request,_range):
     _range = _range.replace('%', ' ')
     start,end = [int(x) for x in _range.split('-')]

     item = Items.objects.filter(Q(price__gte=start)&Q(price__lte=end))
     if item:
         context = {
            'item' : item
         }
         return render(request,'basic.html',context)
     else:
         return HttpResponseNotFound("No items found here")


def fun6(request,_name):
    users=Users.objects.filter(name=_name)
    if users:
        context = {
            'users' : users
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No users found here")


def fun7(request,_status):
    ord= Orders.objects.filter(status=_status)
    if ord:
        context = {
            'ord': ord
        }
        return render(request, 'basic.html', context)
    else:
        return HttpResponseNotFound("no orders found")

def fun8(request,_name):
    item=Items.objects.filter(name=_name)
    if item:
        context = {
            'item' : item
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No users found here")

def fun9(request,_name):
    categorie=Categories.objects.filter(name=_name)
    if categorie:
        context = {
            'categorie' : categorie
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No categories found here")

def fun(request):
    ganesh=Orders.objects.all().values('user').annotate(total=Sum('total_price')).order_by('total')
    if ganesh:
        context = {
            'ganesh': list(ganesh)
        }
        return JsonResponse(context)


def pricing(request,_price):
    item=Items.objects.filter(Q(price__lte=_price))
    if item:
        context = {
            'item' : item
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No users found here")

def totalprice(request):
    orders=Orders.objects.all().values('user').annotate(total=Sum('total_price')).order_by('total')
    if orders:

        context = {
           'orders' : orders
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No orders found here")

def incart(request,_status):
    ord=Orders.objects.filter(status= _status)
    if ord:

        context = {
           'ord' : ord
           #console.log('hhhhhhhh')
        }
        return render(request,'basic.html',context)
    else:
        return HttpResponseNotFound("No orders found here")

def latest(request):
    users = Users_Form(request.POST or None,request.FILES or None)
    if users.is_valid():
        instance = users.save(commit=False)
        instance.save()
        return HttpResponse('form submitted')
    return render(request,'basic.html',{'users':users})
