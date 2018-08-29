from django.contrib import admin
from django.conf.urls import include, url
from DETAILS import urls
from django.http import HttpResponse
from django.conf import  settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^DETAILS/', include('DETAILS.urls')),
]
