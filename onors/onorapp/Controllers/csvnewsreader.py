from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse,HttpResponse,StreamingHttpResponse
from onorapp.models import newsReader
from onorapp.mails.newsreader_mail import news_email
from django.http import Http404
from rest_framework import status
import os.path



def queryset():
        return newsReader.objects.all()


def newsreader_csv(request):
    import csv
    from django.utils.encoding import smart_str
    w=open('/home/ganesh/dev3/onor/onors/onorapp/files/newsreader.csv','w')
    writer = csv.writer(w)
    writer.writerow([
        'ID',
        'email',
    ])
    data = queryset()
    for obj in data:
        writer.writerow([
            obj.pk,
            obj.email,
        ])
    w.close()
    news_email.send()
    return JsonResponse({"sucess":True})
