import re
import sys
from itertools import groupby
import pandas as pd

Input = open(sys.argv[1],'r')
input_data = Input.readlines()

modified_data = []
for x in input_data:
    if re.search(r'^001:',x):
        modified_data.append(x)
    if re.search(r'^002:',x):
        modified_data.append(x)
indexes = []
for x in modified_data:
    if re.search(r'^001:',x):
        a = modified_data.index(x)
        indexes.append(a)
total_data = [modified_data[i : j] for i, j in zip([0] + indexes, indexes + [None])] 

unwanted_data = []
for x in total_data:
    for y in x:
        if re.search(r'-|1$',y[71:91]):
            unwanted_data.append(y)
        if y[31:39] == "Paid Out":
            unwanted_data.append(y)

data_filtering = []
for x in total_data:
    filtering_data = [ele for ele in x if ele not in unwanted_data]
    data_filtering.append(filtering_data)
dt = []
for x in data_filtering:
    d = []
    li = []
    da = []
    for y in x: 
        d1 = []
        if re.search(r'^001:',y):
            # da.append(y[0:4])
            da.append(y[18:24])
            da.append(y[47:87])
            da.append(y[87:127])
            da.append(y[345:373])
        else:
            d1.append(y[11:19])
            d1.append(y[19:27])
            d1.append(y[31:71])
            d1.append(y[71:83])
            
        d.append(da+d1) 
    dt.append(d)
unwanted_data1 = []
for x in dt:
   if len(x) == 0:
       unwanted_data1.append(x)
   elif len(x) == 1:
       unwanted_data1.append(x)

data_modifing1 = [ele for ele in dt if ele not in unwanted_data1]

zzz_data = []
for x in data_modifing1:
   if re.search(r'^ZZZ',x[1][2]):
       zzz_data.append(x)
data_modified = [ele for ele in data_modifing1 if ele not in zzz_data]
# headers = ["Room_No", "First_Name", "Last_Name", "Folio_Num"]
column_names = ["Room_No", "First_Name", "Last_Name", "Folio_Num", "Tran_date","Code", "Description", "Amount"]
tot_data = []
for x in data_modified:
    if len(x) == 1:
        pass
        # print(x)
        # assert3 = {k: v for k, v in zip(headers, x[0])}
        # tot_data.append(assert3)
        pass
    elif len(x) != 0:
        x.pop(0)
        for y in x:
            assert4 = {k: v for k, v in zip(column_names, y)}
            tot_data.append(assert4)
for x in tot_data:
    v = x['Amount']
    vi = v[:10]+'.'+v[10:12]
    x['Amount'] = vi
# print(len(tot_data))
for x in tot_data:
    ind_t=tot_data.index(x)
    if re.search(r' Liquor ',x['Description']):
        tot_data.pop(ind_t)
    if x['Description'] == 'Bar Lunch Liquor                        ':
        tot_data.pop(ind_t)
    if x['Description'] == 'Minibar Liquor                          ':
        tot_data.pop(ind_t)    
    else:
        pass
# print(len(tot_data))

df = pd.DataFrame(tot_data)

# df.to_csv("/home/ganesh/hotel1.csv", index=False)

trans_codes = {"MiniBar_Chocolate":["3008","6923","7316","7317"],"MINIBAR_FOOD":["3000","3003","6920","7314","7315"],"MiniBarSBev_Water":["3001","3009","6921"],
"ACCOMODATION":['9999','1000','1001','1002','1003','1004','1005','1006','1008','1009','1010','1011','1017','1019','1020','1022','1023','1024','1030','1031','1032','1033','1060','2010','2041','2042','6000','6001','6002','6003','6005','6019','6500','6501','6502','6503','6054','6505','6555','6556','7300','7301','7302','7303','7304','7305'],
"FOOD_SBEV":["2000","2001","2010","2011","2035","2036","2110","2111","2200","2201","2220","2221","2240","2241","2300","2301","2320","2321","2380","2381","2400","2401","2403","2404","2407","2420","2421","2531","2600","2601","2700","2701","2760","2761","2800","2801","6100","6101","6111","6140","6141","6150","6153","6154","6180","6210","6380","6381","6506","6507","6508","6509","6510","6511","6512","6513","6600","6680","6681","6760","6761","6880","6881","7306","7307","7308","7309","7310","7311","7312","7313"],
"BanquetsF_SB":
["2050","2051","2080","2081","2680","2681","3100","3101","3108","3130","3131","3138","3150","3151","6660","6700","6701","6800","6801","6910","6913","6930","7321","7322","7327","7328"],
"TRANSPORT":["5205","5207","5218","6547","6548","7005","7010","7347","7348"],
"LAUNDRY1":["2530"],"BANQUET_HALLHIRE":["3500","3506","5234","5235","6523","6524","7323","7324"],
"MISC_Banquets":['3502','3503','3508','3509','5010','6525','6526','6912','6917','7325','7326','7349'],
"TELEPHONE":["4000","4001","4002","4003","4008","6543","6544","7108","7280","7281","7282","7283","7284","7288","7290","7343","7344"],
"WIFI":["4005","4006","4009","4011","6541","6542","7341","7342","7350","7351"],
"TOBACCO":['2002','2012','2037','2052','2112','2202','2242','2222','2302','2322','2382','2402','2422','2532','2602','2682','2702','2762','2802','3102','3132','3152','5202','6103','6112','6142','6152','6182','6212','6302','6322','6382','6402','6422','6529','6530','6531','6532','6533','6534','6602','6682','6702','6762','6782','6802','6882','6932','6962','7002','7329','7330','7331','7332','7333','7334'],
"Laundry":["5001","5003","6545","6546","7062","7063","7345","7346"],
"HEALTHCLUB":["5200","5201","6535","6536","7004","7335","7336"],"SPA":["3600","3601","3602","3603","3605","3606","3607","3608","3609","6537","6538","7337","7338"]}  

MiniBar_Chocolate = []
MINIBAR_FOOD = []
MiniBarSBev_Water=[]
ACCOMODATION =[]
FOOD_SBEV = []
BanquetsF_SB = []
TRANSPORT =[]
LAUNDRY1 = []
BANQUET_HALLHIRE = []
MISC_Banquets = []
TELEPHONE = []
WIFI = []
TOBACCO =[]
Laundry = []
HEALTHCLUB = []
SPA = []
Remaining = []
for x in tot_data:
    co = x["Code"].strip(" ")
    if co in trans_codes['MiniBar_Chocolate']:
        MiniBar_Chocolate.append(x)
    elif co in trans_codes['MINIBAR_FOOD']:
        MINIBAR_FOOD.append(x)
    elif co in trans_codes['MiniBarSBev_Water']:
        MiniBarSBev_Water.append(x)    
    elif co in trans_codes['ACCOMODATION']:
        ACCOMODATION.append(x)
    elif co in trans_codes['FOOD_SBEV']:
        FOOD_SBEV.append(x)
    elif co in trans_codes['BanquetsF_SB']:
        BanquetsF_SB.append(x)               
    elif co in trans_codes['TRANSPORT']:
        TRANSPORT.append(x)      
    elif co in trans_codes['LAUNDRY1']:
        LAUNDRY1.append(x)
    elif co in trans_codes['BANQUET_HALLHIRE']:
        BANQUET_HALLHIRE.append(x)
    elif co in trans_codes['MISC_Banquets']:
        MISC_Banquets.append(x)
    elif co in trans_codes['TELEPHONE']:
        TELEPHONE.append(x)
    elif co in trans_codes['WIFI']:
        WIFI.append(x)
    elif co in trans_codes['TOBACCO']:
        TOBACCO.append(x)
    elif co in trans_codes['Laundry']:
        Laundry.append(x)
    elif co in trans_codes['HEALTHCLUB']:
        HEALTHCLUB.append(x)
    elif co in trans_codes['SPA']:
        SPA.append(x)
    else:
        Remaining.append(x)

csv_data=[]
def fun(llist,name):
    Total_amount = 0
    Sgst_amount_9 = 0
    Cgst_amount_9 = 0
    Sgst_amount_14 = 0
    Cgst_amount_14 = 0
    Sgst_amount_6 = 0
    Cgst_amount_6 = 0
    for x in llist:
        vv= x['Description']
        v =vv[6:9]
        if "SGST" in x['Description']:
            if re.search(r'9',v):    
                a = float(x['Amount'])
                Sgst_amount_9+=a
            elif re.search(r'14',v):
                a = float(x['Amount'])
                Sgst_amount_14+=a
            elif re.search(r'6',v):
                a = float(x['Amount'])
                Sgst_amount_6+=a
            else:
                pass        
        elif "CGST" in x['Description']:
            vv= x['Description']
            v =vv[6:9]
            if re.search(r'9',v):
                a = float(x['Amount'])
                Cgst_amount_9+=a
            elif re.search(r'14',v):
                a = float(x['Amount'])
                Cgst_amount_14+=a
            elif re.search(r'6',v):
                a = float(x['Amount'])
                Cgst_amount_6+=a
            else:
                pass
           
        else:
            a = float(x['Amount'])
            Total_amount+=a
    d={"Name":name,"Total_amount":Total_amount,"Total_Sgst_14":Sgst_amount_14,
        "Total_Sgst_9":Sgst_amount_9,"Total_Sgst_6":Sgst_amount_6,
        "Total_Cgst_14":Cgst_amount_14,"Total_Cgst_9":Cgst_amount_9,"Total_Cgst_6":Cgst_amount_6}
    # print(d)
    csv_data.append(d)       
    # print("---------------------------------------------------")


fun(ACCOMODATION,"ACCOMODATION")
fun(MiniBar_Chocolate,"MiniBar_Chocolate")
fun(MINIBAR_FOOD,"MINIBAR_FOOD")
fun(MiniBarSBev_Water,"MiniBarSBev_Water")
fun(FOOD_SBEV,"FOOD_SBEV")
fun(BanquetsF_SB,"BanquetsF_SB")
fun(TRANSPORT,"TRANSPORT")
fun(LAUNDRY1,"LAUNDRY1")
fun(BANQUET_HALLHIRE,"BANQUET_HALLHIRE")
fun(MISC_Banquets,"MISC_Banquets")
fun(TELEPHONE,"TELEPHONE")
fun(WIFI,"WIFI")
fun(TOBACCO,"TOBACCO")
fun(Laundry,"Laundry")
fun(HEALTHCLUB,"HEALTHCLUB")
fun(SPA,"SPA")
print(csv_data,len(csv_data))
cc = pd.DataFrame(csv_data)
cc.to_csv("/home/ganesh/ccc.csv",index = False)




























# df = pd.DataFrame(tot_data)

# df.to_csv("/home/ganesh/hotel.csv", index=False)
# import csv
# employ_data = open('/home/ganesh/hotel.csv', 'w')
# csvwriter = csv.writer(employ_data)
# count = 0
# for emp in tot_data:
#      if count == 0:
#             header = emp.keys()
#             csvwriter.writerow(header)
#             count += 1
#      csvwriter.writerow(emp.values())
# employ_data.close()


        