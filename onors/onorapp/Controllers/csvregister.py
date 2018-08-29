from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse,StreamingHttpResponse
from onorapp.models import Registers
from onorapp.mails.registerslist_mail import email
from django.http import Http404
from rest_framework import status
import csv
from django.utils.encoding import smart_str




def queryset():
        return Registers.objects.all()


def export_csv(request):
    w=open('/home/ganesh/dev3/onor/onors/onorapp/files/Registers.csv','w')
    writer = csv.writer(w)
    writer.writerow([
        'ID',
        'first_name',
        'mobile_no',
        'email',
        'enquiry',
    ])
    data = queryset()
    for obj in data:
        writer.writerow([
            obj.pk,
            obj.first_name,
            obj.mobile_no,
            obj.email,
            obj.enquiry
        ])
    w.close()
    email.send()
    return JsonResponse({"sucess":True})
