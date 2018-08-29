from rest_framework.decorators import api_view,APIView
from .serializers import BillDetailsSerializer,InventorySerilaizer,BillsSerializer
from .models import BillDetails,Inventory
from rest_framework.response import Response
from django.db.models import F,Sum
from rest_framework.fields import empty
from django.forms.models import model_to_dict
from collections import Counter



@api_view(['GET'])
def fun(request):
    s=Inventory.objects.all()
    o=InventorySerilaizer(s,many=True)
    return Response(o.data)


@api_view(['POST'])
def puting(request):
    s=InventorySerilaizer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status= 301)



@api_view(['PUT'])
def update(request,id):
  print(request.data)
  a=Inventory.objects.filter(id=id).first()
  #b = dict([obj.as_dict() for obj in a])
  b=model_to_dict(a)
  print(b)
  z=dict(Counter(b)+Counter(request.data))
  print(z)
  #.update(z)
  serializer =InventorySerilaizer(a,data=z)
  print(serializer)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status= 301)

@api_view(['PUT'])
def put(request,id):
    a=Inventory.objects.filter(id=id)

    for my_obj in a:
        my_obj.user = request.data.get(my_obj)
        print(my_obj.user)
        se= InventorySerilaizer(data=a)
        if se.is_valid():
            se.save()
            return Response(se.data, status= 301)


@api_view(['POST'])
def addbill(request):
    s=BillDetailsSerializer(data=request.data)
    print(s)

    if s.is_valid():
        s.save()
        return Response(s.data, status= 301)

class like(APIView):
   def get(self, request,*args,**kwargs):
       try:
           get = BillDetails.objects.all()
           serializer = BillDetailsSerializer(get,many=True)
           return Response(serializer.data)
       except Inventory.DoesNotExist:
           raise Http404
   def post(self, request, format=None):
       serializer = BillsSerializer(data=request.data)
       print(request.data)
       print("-------------------------------------------")
       a=Inventory.objects.filter(id=1).first()
       b=model_to_dict(a)
       print(b)
       print("----------------------------------------------")
       v=dict(Counter(b)-Counter(request.data))
       print(v)
       x =InventorySerilaizer(a,data=v)
       if x.is_valid():
           x.save()
       print (serializer)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=301)
       return Response(serializer.errors, status=301)

class dummy(APIView):
   def get(self, request,*args,**kwargs):
       try:
           get = BillDetails.objects.all()
           serializer = BillDetailsSerializer(get,many=True)
           return Response(serializer.data)
       except Inventory.DoesNotExist:
           raise Http404
   def post(self, request, format=None):
       serializer = BillsSerializer(data=request.data)
       print(request.data)
       print("-------------------------------------------")

       #x =InventorySerilaizer(a)

       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=301)
