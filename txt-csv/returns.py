data =[]
import xlwt
from pandas import ExcelWriter
import pandas as pd
with open("/home/ganesh/Documents/Audits/retu.txt") as f:
    for line in f:
        data.append(line)
full_list=[]
modified_headers=[]
Headers = data[1:7]
num = 7
length = len(data)
for x in Headers:
    a=x.replace("|",",")
    b=a.replace(" ","") 
    modified_headers.extend(b.split(","))
for x in modified_headers:
    if x == "\n":
        modified_headers.remove(x)
str_list = [x for x in modified_headers if x != '']
v=[]

for x in str_list:
    a = x.strip("\n")    
    z=a.lstrip('0123456789.- ')   
    v.append(z)
v[7]='Alloc?'
v.insert(8,'Live?')
data_list=[]
for i in range(7,length,7):
    x = data[i+1:i+num]
    full_list.append(x)
modified_data = [] 
fun =  [full_list[i:i+10] for i in range(0, len(full_list), 10)]
n=1
for i in range(0,10):
    l= full_list[i]
    modified_list=[]
    le = len(full_list[1])
    nn = len(modified_headers)
    for x in l:
        m = x.strip("\n")
        a=m.replace("|",",")
        b=a.replace(" ","")
        modified_list.extend(b.split(","))
        modified_list = [x for x in modified_list if x != '']    
    modified_data.append(modified_list)
mo_data=[]
for a in modified_data:
    mo_list =[]
    nnn= len(a)
    for x in a:
        ind = a.index(x)
        if ind ==11:
            iii = 11
            end = len(x)
            # print(end)
            inn = str(iii)
            vv = x[len(inn):end]
            print(cb)
            mo_list.append(vv)
            print(mo_list)
        else:    
            end = len(x)
            inn = str(ind)
            cb = x[len(inn):end]
            mo_list.append(cb)
    mo_list[7]='No'
    mo_list.insert(8,'Yes')
    mo_list.insert(11,vv)
    mo_list[30]='PRI'
    mo_list[24]='DL'    
    mo_list[6]=''
    # print(mo_list[11])    
    mo_data.append(mo_list)
z = []
for x in mo_data:
   z.append(dict(zip(v, x)))
import csv
employ_data = open('/home/ganesh/Return.csv', 'w')
csvwriter = csv.writer(employ_data)
count = 0
for emp in z:
     if count == 0:
            header = emp.keys()
            csvwriter.writerow(header)
            count += 1
     csvwriter.writerow(emp.values())
employ_data.close()

     



    





    


