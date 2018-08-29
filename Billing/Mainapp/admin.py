from django.contrib import admin

from .models import Inventory,BillDetails



class InventoryDetail(admin.ModelAdmin):
    list_display = ("id","Rs2000","Rs500","Rs100","Rs50","Rs20","Rs10","Rs5","Rs2","Rs1")
admin.site.register(Inventory,InventoryDetail)

class BillDetailsDetail(admin.ModelAdmin):
    list_display = ("id","bill","paid","change","Rs2000","Rs500","Rs100","Rs50","Rs20","Rs10","Rs5","Rs2","Rs1")
admin.site.register(BillDetails,BillDetailsDetail)
