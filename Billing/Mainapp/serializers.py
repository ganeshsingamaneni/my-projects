from rest_framework import serializers
from .models import Inventory,BillDetails
from django.forms.models import model_to_dict
from collections import Counter
import re

class InventorySerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Inventory
        fields = '__all__'


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta():
        model = BillDetails
        fields = ('bill','paid','change','Rs2000','Rs500','Rs100','Rs50','Rs20','Rs10','Rs5','Rs2','Rs1')
        extra_kwargs = {'change':{'read_only':True,},'Rs2000':{'read_only':True,},'Rs500':{'read_only':True,},'Rs100':{'read_only':True,},
                         'Rs50':{'read_only':True,},'Rs20':{'read_only':True,},'Rs10':{'read_only':True,},'Rs50':{'read_only':True,},
                         'Rs2':{'read_only':True,},'Rs1':{'read_only':True,},}

    def create(self, validated_data):

        bill= validated_data['bill']
        paid = validated_data['paid']
        change = paid - bill
        obj = BillDetails(bill=bill, paid=paid, change=change,Rs2000=Rs2000,Rs500=Rs500,Rs100=Rs100,Rs50=Rs50,Rs20=Rs20,Rs10=Rs10,Rs5=Rs5,Rs2=Rs2,Rs1=Rs1)
        obj.save()
        return obj
class BillsSerializer(serializers.ModelSerializer):
    class Meta():
        model = BillDetails
        fields = ('bill','paid','change','Rs2000','Rs500','Rs100','Rs50','Rs20','Rs10','Rs5','Rs2','Rs1')
        extra_kwargs = {'change':{'read_only':True,},'Rs2000':{'read_only':True,},'Rs500':{'read_only':True,},'Rs100':{'read_only':True,},
                         'Rs50':{'read_only':True,},'Rs20':{'read_only':True,},'Rs10':{'read_only':True,},'Rs50':{'read_only':True,},
                         'Rs2':{'read_only':True,},'Rs1':{'read_only':True,},}

    def create(self, validated_data):
       bill= validated_data['bill']
       paid = validated_data['paid']
       change = paid-bill
       get = change
       ram=Inventory.objects.filter(id=1).first()
       b=model_to_dict(ram)
       print("getting:",b)
       l=[]
       k=b.keys()
       print(k)
       v=b.values()
       print(v)
       h=Inventory.objects.filter(id=2).first()
       g=model_to_dict(h)
       f={key:values for key,values in g.items() if key!='id' }
       print("delate:",f)
       inv=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in g.items() if key!='id']
       mon=[]
       z=f.values()
       print(z)
       for u,x in inv:
           mon.append(int(x))
       print("fuc:",(mon))
       dic=dict(zip(mon,z))
       print("zero:",dic)
       d=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in b.items() if key!='id']
       print("fsfsbhdf:",d)
       for w,q in d:
           l.append(int(q))
       denoms=sorted(l,reverse=True)
       print("denoms:",denoms)
       while (get > 0):
           if (get >= denoms[0]):
               num = get // denoms[0]
               get -= (num * denoms[0])
               dec={denoms[0]:num}
               dic.update(dec)
               print("bjbdfb:",dic)
           denoms = denoms[1:]
       obj = BillDetails(bill=bill, paid=paid,change=change,Rs2000=dic[2000],Rs500=dic[500],Rs100=dic[100],Rs50=dic[50],Rs20=dic[20],Rs10=dic[10],Rs5=dic[5],Rs2=dic[2],Rs1=dic[1])
       obj.save()
       q=model_to_dict(obj)
       v=dict(Counter(b)-Counter(q))
       x =InventorySerilaizer(ram,data=v)
       if x.is_valid():
           x.save()
       return obj
