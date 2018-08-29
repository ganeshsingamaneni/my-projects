from django.conf.urls import url,include
from django.urls import path
from .rest_api import test,addcategories,addusers,additems,addorders,getcategories
from .rest_api import getitems,getusers,getorders,updateitems,updateusers,updateorders,updatecategories
from .rest_api import deletecategories
from .views import orders,items,users,categories,pricerange,fun6,fun7,fun8,fun9,fun,pricing,totalprice,incart,latest
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



urlpatterns = [
    url(r'^testcase', test),
    url(r'^addc',addcategories),
    url(r'^addu',addusers),
    url(r'^addi',additems),
    url(r'^addo',addorders),
    url(r'^getc',getcategories),
    url(r'^geti',getitems),
    url(r'^getu',getusers),
    url(r'^geto',getorders),
    url(r'^updateo/(?P<_status>[0-99,-]+)',updateorders),
    url(r'^updatei/(?P<_name>[\w\-]+)/$',updateitems),
    url(r'^updateu/(?P<_name>[\w\-]+)/$',updateusers),
    url(r'^updatec/(?P<_name>[\w\-]+)/$',updatecategories),
    url(r'^deletec/(?P<_name>[\w\-]+)/$',deletecategories),
    url(r'^orders',orders),
    url(r'^items',items),
    url(r'^users',users),
    url(r'^categorie',categories),
    url(r'^pricerange/(?P<_range>[0-99,-]+)',pricerange),
    url(r'^fun6/(?P<_name>[\w\-]+)/$',fun6),
    url(r'^fun7/(?P<_status>[0-99,-]+)',fun7),
    url(r'^fun8/(?P<_name>[\w\-]+)/$',fun8),
    url(r'^fun9/(?P<_name>[\w\-]+)/$',fun9),
    url(r'^fun/',fun),
    url(r'^price/(?P<_price>[0-99,-]+)',pricing),
    url(r'^totalprice',totalprice),
    url(r'^incart/(?P<_status>[0-99,-]+)',incart),
    url(r'^latest',latest),
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    
]
