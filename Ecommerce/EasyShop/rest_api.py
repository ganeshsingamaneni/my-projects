from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from .models import Categories, Items, Users, Orders
from EasyShop.serializers import CategoriesSerializer,ItemsSerializer,UsersSerializer,OrdersSerializer




@api_view(['GET'])
def test(request):
    return Response({'hiii':'everyone','how is it':'working succesfully'})

@api_view(['POST'])
def addcategories(request):

    serializer = CategoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)
    else:
        return Response({'POST':'not working'})

@api_view(['POST'])
def addusers(request):
    s = UsersSerializer(data = request.data)
    if s.is_valid():
        s.save()
        return Response(s.data,status = 301)
    else:
        return Response({'POST':'not working'})

@api_view(['POST'])
def additems(request):
    serializer = ItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)
    #else:
    #    return Response({'POST':'not working'})


@api_view(['POST'])
def addorders(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)
    else:
        return Response({'POST':'not working'})


@api_view(['GET'])
def getcategories(request):
    s=Categories.objects.all()
    if s:
        obj= CategoriesSerializer(s,many= True)
        return Response(obj.data)

@api_view(['GET'])
def getitems(request):
    s=Items.objects.all()
    if s:
        obj= ItemsSerializer(s,many= True)
        return Response(obj.data)

@api_view(['GET'])
def getusers(request):
    s=Users.objects.all()
    if s:
        obj= UsersSerializer(s,many= True)
        return Response(obj.data)

@api_view(['GET'])
def getorders(request):
    s=Orders.objects.all()
    if s:
        obj= OrdersSerializer(s,many= True)
        return Response(obj.data)


@api_view(['PUT'])
def updatecategories(request,_name):
    s=Categories.objects.filter(name=request.data['name'])
    s.update(name=request.data["name"])
    ser=CategoriesSerializer(data=s,many=True)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status= 301)

@api_view(['PUT'])
def updateitems(request,_name):
    s=Items.objects.filter(name=request.data['name'])
    s.update(name=request.data["name"])
    ser=ItemsSerializer(data=s,many=True)
    if ser.is_valid():
        ser.save()
        return HttpResponse(ser.data,status= 301)


@api_view(['PUT'])
def updateusers(request,_name):
    s=Users.objects.filter(name=request.data['name'])
    print(s)
    s.update(name=request.data["name"])
    ser=UsersSerializer(data=s,many=True)
    print(ser)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status= 301)



@api_view(['PUT'])
def updateorders(request,_status):
    s=Orders.objects.filter(status=request.data['status'])
    s.update(status=request.data["status"])
    ser=OrdersSerializer(data=s,many=True)
    if ser.is_valid():
        ser.save()
        return get_response({"result":"its worked"},status= 301)

@api_view(['DELETE'])
def deletecategories(request,_name):
    mul = Categories.objects.filter(name=_name)
    mul.delete()
    serializer = CategoriesSerializer(data=mul, many=True)
    if serializer.is_valid():
        serializer.save()
        return HttResponse({"result":"its worked"}, status= 301)
