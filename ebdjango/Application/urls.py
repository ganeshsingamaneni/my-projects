from django.conf.urls import include, url
from django.urls import path
from .views import *
urlpatterns =[
     # url('home', Home),
     url('adduser',Adduser.as_view())
     ]     