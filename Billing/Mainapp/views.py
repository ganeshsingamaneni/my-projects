from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from .models import Inventory,BillDetails
from django.core import serializers
from django.db.models import Q,Sum,Count,Avg,Max
from .forms import Inventory_Form,Bills_Form
#from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from collections import Counter
from .serializers import InventorySerilaizer,BillsSerializer,BillDetailsSerializer
from rest_framework.response import Response




def invent(request):
    act= Inventory.objects.all()
    if ord:
        context = {
            'act': act
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("no orders found")

def totalbills(request):
    serializer= BillDetails.objects.all()
    if serializer:
        context = {
            'serializer': serializer
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("no orders found")



def cost(request):
   act= Inventory_Form(request.POST)
   posting=request.POST
   #print(posting)
   post={}
   a=Inventory.objects.filter(id=1).first()
   b=model_to_dict(a)
   print("getting:",b)
   print("----------------------------------------------------------------------")
   for key,values in posting.items():
      val=values
      for x in val:
          if key!='csrfmiddlewaretoken':
              y=int(x)
              d={key:y}
              post.update(d)
          print("post data:",post)
          print("---------------------------------------------------------------")
   z=dict(Counter(b)+Counter(post))
   print(z)
   if act.is_valid():
       act= Inventory_Form(z,instance=a)
       act.save()
       return HttpResponse('form submited')
   return render(request, 'index.html', {'act': act})



class details():
    def test(request):
        serializer = Bills_Form(request.POST)
        posting=request.POST
        post={}
        bill= validated_data['bill']
        paid = validated_data['paid']
        change = paid - bill
        print("change: ",change)
        print("bill ",bill)
        ch=change
        d={2000:0,500:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
        f=Inventory.objects.filter(id=1).first()
        b=model_to_dict(f)
        print(b)
        denoms=[2000,500,100,50,20,10,5,2,1]
        while (ch > 0):
            if (ch >= denoms[0]):
                num = change // denoms[0]
                ch -= (num * denoms[0])
                dec={denoms[0]:num}
                d.update(dec)
            denoms = denoms[1:]
            obj = BillDetails(bill=bill, paid=paid, change=change,Rs2000=d[2000],Rs500=d[500],Rs100=d[100],Rs50=d[50],Rs20=d[20],Rs10=d[10],Rs5=d[5],Rs2=d[2],Rs1=d[1])
            obj.save()
            q=model_to_dict(obj)
            v=dict(Counter(b)-Counter(q))
            x =Inventory_Form(f,data=v)
            if x.is_valid():
                x.save()
            return obj
        for key,values in posting.items():
            val=values
        for x in val:
            if key!='csrfmiddlewaretoken':
                y=int(x)
                d={key:y}
                post.update(d)
            #print("post data:",post)
            #print("---------------------------------------------------------------")
        a=Inventory.objects.filter(id=1).first()
        b=model_to_dict(a)
        print("b ",b)
        #print("----------------------------------------------------------")
        v=dict(Counter(b)-Counter(post))
        print("v ",v)
        if serializer.is_valid():
            serializer =Inventory_Form(v,instance=a)
            serializer.save()
            return HttpResponse("success")
        return render(request,'index.html',{'serializer':serializer})
