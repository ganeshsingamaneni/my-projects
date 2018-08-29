from django.conf.urls import include, url
from .views import getsubject,getstudentname,getmathstopper,getbeststudents
from .views import gettotal,gettopper,getleaststudent,gethighsubavg
from .views import getstudentid,facultydata,getrange,studentdata,getmarks,getsubavg,geteachsubavg
from .rest_api import test, studentlist,studentmarks,ninty,single,leaststudent,eachsubavg
from .rest_api import mathstopper,bestfaculty,topfaculty,studentstotal,worstfaculty,topstudent
urlpatterns =[
     url(r'^studentid/(?P<_id>\d+)', getstudentid),
     url(r'^studentname/(?P<_studentname>[\w\-]+)/$', getstudentname),
     url(r'^subject/(?P<_subject>[\w\-]+)/$',getsubject),
     url(r'^faculty/',facultydata),
     url(r'^studentmarks/',studentdata),
     url(r'^marks/(?P<_marks>\d+)', getmarks),
     url(r'^range/(?P<_range>[0-99,-]+)',getrange),
     url(r'^maths/',getmathstopper),
     url(r'^gettotal/',gettotal),
     url(r'^subavg/',getsubavg),
     url(r'^topper/',gettopper),
     url(r'^geteachsubavg/',geteachsubavg),
     url(r'^leaststud/',getleaststudent),
     url(r'^highsubavg/',gethighsubavg),
     url(r'^beststudents/',getbeststudents),

         #rest_api
     url(r'^ninty/',ninty),
     url(r'^test/', test),
     url(r'^students/',studentlist),
     url(r'^apimarks/(?P<_marks>\d+)', studentmarks),
     url(r'^single/',single),
     url(r'^mathstopper/',mathstopper),
     url(r'^bestfaculty/',bestfaculty),
     url(r'^topfaculty/',topfaculty),
     url(r'^studentstotal/',studentstotal),
     url(r'^worstfaculty/',worstfaculty),
     url(r'^topstudent/',topstudent),
     url(r'^leaststudent/',leaststudent),
     url(r'^eachsubavg/',eachsubavg)

]
