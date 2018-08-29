from django.conf.urls import url
from .rest_api import fun,puting,put,addbill,update,like,dummy
from .views import invent,totalbills,details,cost
urlpatterns = [

            url(r'^fun',fun),
            url(r'^put',puting),
            url(r'^update/(?P<id>[0-99,-]+)',update),
            #url(r'^add/(?P<id>[0-99,-]+)',add),
            url(r'^update/(?P<id>[0-99,-]+)',put),
            url(r'^addbill',addbill),
            url(r'^like',like.as_view()),
            url(r'^invent',invent),
            url(r'^totalbills',totalbills),
            url(r'^dummy',dummy.as_view()),
            url(r'^cost',cost),
            url(r'^details/',details),

]
