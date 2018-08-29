from django.contrib import admin

from .models import Items,Users,Orders,Categories


class CategoriesDetail(admin.ModelAdmin):
    list_display = ('id','name','status')
admin.site.register(Categories,CategoriesDetail)

class ItemsDetail(admin.ModelAdmin):
    list_display = ('id','name','price','status','images','files')
admin.site.register(Items,ItemsDetail)


class UsersDetail(admin.ModelAdmin):
    list_display = ('id','name','address')
admin.site.register(Users,UsersDetail)


class OrdersDetail(admin.ModelAdmin):
    list_display = ('status','total_price','status')
admin.site.register(Orders,OrdersDetail)
