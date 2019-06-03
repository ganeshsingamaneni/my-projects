import re
headers = ['G.L. Name', 'Balance','Total']
data = []
Input = open("/home/ganesh/pdf2.txt",'r')
input_data = Input.readlines()
# print(len(input_data))
unwanted = ["Current Date :","Reg. No.","Balance Sheet","Liabilities,Assets","Liabilities,,Assets","Page","As On Date","G.L. Name Balance,Total","Clerk Manager"]
for x in unwanted:
    for y in input_data:
        if x in y:
            input_data.remove(y)

assests =[]
liabilities=[]
def assests():
    for x in input_data:
        if re.search(r"\.\d{2},|\["",]",x):
            d = re.split(r"\,",x)
            d1 = d[0]
            d11 = d[1]
            d2 = re.sub(r"\  ","|",d1,3)
            d3 = re.split(r"\|",d2)
            if len(d3) == 2:    
                d3.insert(2,' ')
                assests.append(d3)
            else:
                d4 = []
                l = len(d3)
                if l == 3:
                    v = d3[0]+d3[1]
                    d4.insert(0,v)
                    d4.insert(1,d3[2])
                    assests.append(d4)
                elif l == 4:
                    v = d3[0]+d3[1]+d3[2]
                    d4.insert(0,v)
                    d4.insert(1,d3[3])
                    assests.append(d4)
        else:
            if x.startswith('"",'):
                pass
            else:
                da = re.sub(r"\  |\.00","|",x,1)
                db = re.split(r"\|",da)
                dc = db[0]
                d5=dc.split(",")
                d5.insert(1,'') 
                assests.append(d5)
def Liabilities():
    data =[]
    for x in input_data:
        # print(x)
        if re.search(r"\.\d{2},|\["",]",x):
            d = re.split(r"\,",x)
            d.pop(0)    
            le = len(d)
            if le == 3:
                d.pop(1)
                data.append(d)
            if le == 4:
                d.pop(2)
                data.append(d)
            if le == 5:
                d.pop(3)
                data.append(d)
        elif x.startswith('"",'):
            # print(x,type(x))
            d = re.split(r"\,",x)
            d.pop(0)    
            # print("1", d,len(d))
            # if d[0].startswith('"')    
        else:
            pass
    print(data)                
Liabilities()
# print(assests,len(assests))
# z=[]
# for x in assests:
#    z.append(dict(zip(headers, x)))
# import csv
# employ_data = open('/home/ganesh/assests.csv', 'w')
# csvwriter = csv.writer(employ_data)
# count = 0
# for emp in z:
#      if count == 0:
#             header = emp.keys()
#             csvwriter.writerow(header)
#             count += 1
#      csvwriter.writerow(emp.values())
# employ_data.close()
# import image_slicer
# image_slicer.slice('/home/ganesh/page_2.jpg', 2)