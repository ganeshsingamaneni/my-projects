from django.conf.urls import url

from .views import create,show
from .restapi import getapi,post
urlpatterns = [
    url(r'create/',create),
    url(r'show/',show),
    url(r'get/',getapi),
    url(r'post/(?P<_question>[A-Za-z%]+)$',post)

]
 #url(r'^(?P<_subject>[A-Za-z%]+)$', getsubject),
