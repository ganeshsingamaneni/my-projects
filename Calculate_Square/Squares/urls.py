from django.conf.urls import include, url
from django.http import HttpResponse
from views import getsquare,postdata,post


urlpatterns =[
    url(r'^getsqr/(?P<_num>\d+)', getsquare),
    url(r'^add/', postdata),
    url(r'^post/(?P<_Number>\d+)',post)
]
