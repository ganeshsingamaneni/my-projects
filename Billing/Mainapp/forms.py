from django import forms
from .models import BillDetails,Inventory

class Inventory_Form(forms.ModelForm):
    class Meta:
        model=Inventory
        fields = ('Rs2000','Rs500','Rs20','Rs100','Rs50','Rs20','Rs10','Rs5','Rs2','Rs1')


class Bills_Form(forms.ModelForm):
    class Meta():
        model = BillDetails
        fields = ('bill','paid')
        extra_kwargs = {'change':{'read_only':True,},'Rs2000':{'read_only':True,},'Rs500':{'read_only':True,},'Rs100':{'read_only':True,},
                          'Rs50':{'read_only':True,},'Rs20':{'read_only':True,},'Rs10':{'read_only':True,},'Rs50':{'read_only':True,},
                           'Rs2':{'read_only':True,},'Rs1':{'read_only':True,},}
