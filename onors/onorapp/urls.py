from django.conf.urls import include,url
from onorapp.Controllers.Roles import getUpdateRoles
from onorapp.Controllers.PostRoles import addRoles
from onorapp.Controllers.User import getUpdateDeleteUsers,PasswordReset
from onorapp.Controllers.PostUsers import addUsers
from onorapp.Controllers.Carousel import getUpdateDeleteCarousel
from onorapp.Controllers.PostCarousel import addCarousel
from onorapp.Controllers.Categories import getUpdateDeleteCategories
from onorapp.Controllers.PostCategories import addCategories
from onorapp.Controllers.PostRegisters import addRegisters
from onorapp.Controllers.Registers import getUpdateDeleteRegisters
from onorapp.Controllers.PostVideo import addVideos
from onorapp.Controllers.Video import getUpdateDeleteVideos
from onorapp.Controllers.CategoryCarousel import getUpdateDeleteCategoryCarousel
from onorapp.Controllers.PostCategoryCarousel import addCategoryCarousel
from onorapp.Controllers.CategoryList import getUpdateDeleteCategoryList
from onorapp.Controllers.PostCategoryList import addCategoryList
from onorapp.Controllers.CategoryListImages import getUpdateDeleteItemImages
from onorapp.Controllers.PostCategoryListImages import createItemImages
from onorapp.Controllers.login_api import login
from onorapp.Controllers.getcategoriecarousel import getCategoryCarousel
from onorapp.Controllers.getcategorylist import getCategoryList
from onorapp.Controllers.getitemvideos import getItemVideos
from onorapp.Controllers.getitemimages import getItemImages
from onorapp.Controllers.getstatusactive import getcategorystatus,getuserstatus,getrolesstatus
from onorapp.Controllers.getstatusactive import getcarouselstatus,getcategorycarouselstatus
from onorapp.Controllers.getstatusactive import getcategoryliststatus,getcategorylistimagestatus
from onorapp.Controllers.getstatusactive import getvideostatus
from onorapp.Controllers.getcategorie_carouselstatus import CategoryCarouselstatus
from onorapp.Controllers.post_news_reader import addnewsreader
from onorapp.Controllers.newsreader import getUpdateDeletenewsreader
from onorapp.Controllers.csvregister import export_csv
from onorapp.Controllers.csvnewsreader import newsreader_csv

urlpatterns=[
     url(r'^getupdateroles/(?P<id>\d+)$',getUpdateRoles.as_view()),
     url(r'^addroles',addRoles.as_view()),
     url(r'^getupdatedeleteusers/(?P<id>\d+)$',getUpdateDeleteUsers.as_view()),
     url(r'^resetpassword/(?P<id>\d+)$',PasswordReset.as_view()),
     url(r'^addusers',addUsers.as_view()),
     url(r'^getupdatedeletecarousel/(?P<id>\d+)$',getUpdateDeleteCarousel.as_view()),
     url(r'^addcarousel',addCarousel.as_view()),
     url(r'^getupdatedeletecategories/(?P<id>\d+)$',getUpdateDeleteCategories.as_view()),
     url(r'^addcategories',addCategories.as_view()),
     url(r'^addregisters',addRegisters.as_view()),
     url(r'^getupdatedeleteregisters/(?P<id>\d+)$',getUpdateDeleteRegisters.as_view()),
     url(r'^getupdatedeletecategorycarousel/(?P<id>\d+)$',getUpdateDeleteCategoryCarousel.as_view()),
     url(r'^addcategorycarousel',addCategoryCarousel.as_view()),
     url(r'^getupdatedeletecategorylist/(?P<id>\d+)$',getUpdateDeleteCategoryList.as_view()),
     url(r'^addcategorylist',addCategoryList.as_view()),
     url(r'^getupdatedeleteitemimages/(?P<id>\d+)$',getUpdateDeleteItemImages.as_view()),
     url(r'^additemimages',createItemImages.as_view()),
     url(r'^getupdatedeletevideos/(?P<id>\d+)$',getUpdateDeleteVideos.as_view()),
     url(r'^addvideos',addVideos.as_view()),
     url(r'^getcategorycarousel/(?P<id>\d+)$',getCategoryCarousel.as_view()),
     url(r'^getcategorylist/(?P<id>\d+)$',getCategoryList.as_view()),
     url(r'^getitemimages/(?P<id>\d+)$',getItemImages.as_view()),
     url(r'^getitemvideos/(?P<id>\d+)$',getItemVideos.as_view()),
     url(r'^getcategorystatus',getcategorystatus.as_view()),
     url(r'^getuserstatus',getuserstatus.as_view()),
     url(r'^getrolesstatus',getrolesstatus.as_view()),
     url(r'^getcarouselstatus',getcarouselstatus.as_view()),
     url(r'^getvideostatus',getvideostatus.as_view()),
     url(r'^getcategorycarouselstatus',getcategorycarouselstatus.as_view()),
     url(r'^getcategoryliststatus',getcategoryliststatus.as_view()),
     url(r'^getcategorylistimagestatus',getcategorylistimagestatus.as_view()),
     url(r'^login',login.as_view()),
     url(r'^getstatusofcategorycarousel/(?P<id>\d+)$',CategoryCarouselstatus.as_view()),
     url(r'^addnewsreader',addnewsreader.as_view()),
     url(r'^getupdatedeletenewsreader/(?P<id>\d+)$',getUpdateDeletenewsreader.as_view()),
     url(r'^registercsv',export_csv),
     url(r'^newsreadercsv',newsreader_csv)

]
