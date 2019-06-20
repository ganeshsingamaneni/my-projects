import re
import os
import sys
import logging 
import traceback
from itertools import groupby
import pandas as pd

# opening file and reading lines in it
Input = open(sys.argv[1],'r')
head, tail = os.path.split(sys.argv[1])
file_name = tail.split(".")
input_data = Input.readlines()

file_handler = logging.FileHandler(filename=os.getcwd()+'/'+file_name[0]+'.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',handlers=handlers)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG) 
logger.info("Data parsing started") 



# Dictionary with keys as Sac code names and values as list of different codes of sac code
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
"Liquor":['2006','2016','2046','2056','2116','2206','2226','2246','2306','2326','2386','2406','2426','2536','2606','2680','2706','2766','2806','3002','3004','3005','3106','3136','3156','6116','6146','6156','6216','6306','6326','6386','6406','6426','6606','6686','6706','6707','6766','6786','6806','6886','6922','6926','6936','6966'],
"HEALTHCLUB":["5200","5201","6535","6536","7004","7335","7336"],"SPA":["3600","3601","3602","3603","3605","3606","3607","3608","3609","6537","6538","7337","7338"]}  

def fun(llist):
    # function to calculate amount,sgst,sgst,cess for folio number based on each sac code 
    Total_amount = 0
    Sgst_amount_9 = 0
    Cgst_amount_9 = 0
    Sgst_amount_14 = 0
    Cgst_amount_14 = 0
    Sgst_amount_6 = 0
    Cgst_amount_6 = 0
    Cess_amount = 0
    for x in llist:
        room_num = x['Room_No']
        name = x['First_Name'].strip(" ")+' '+x['Last_Name'].strip(" ")
        folio_number = x['Folio_Num']
        description_in_x= x['Description']
        description =description_in_x[6:9]
        sac_code = x['SAC_Code']
        category = x['Category']
        if "SGST" in x['Description']:
            if re.search(r'9',description):
                gst_per_number = '9'    
                amount = float(x['Amount'])
                Sgst_amount_9 += amount
            elif re.search(r'14',description):
                gst_per_number = '14'
                amount = float(x['Amount'])
                Sgst_amount_14 += amount
            elif re.search(r'6',description):
                gst_per_number = '6'
                amount = float(x['Amount'])
                Sgst_amount_6 += amount
            else:
                pass        
        elif "CGST" in x['Description']:
            description_in_x = x['Description']
            description = description_in_x[6:9]
            if re.search(r'9',description):
                amount = float(x['Amount'])
                Cgst_amount_9 += amount
            elif re.search(r'14',description):
                amount = float(x['Amount'])
                Cgst_amount_14 += amount
            elif re.search(r'6',description):
                amount = float(x['Amount'])
                Cgst_amount_6 += amount
            else:
                pass
        elif "Cess R" in x['Description']:
            amount  = float(x['Amount'])
            Cess_amount += amount

        else:
            amount = float(x['Amount'])
            Total_amount += amount 
    gst_28 = Sgst_amount_14+Cgst_amount_14
    gst_18 = Sgst_amount_9+Cgst_amount_9
    gst_12 = Sgst_amount_6+Cgst_amount_6 
    
               
    total_invoice = Total_amount + gst_28 + gst_18 + gst_12
    total_tax =  gst_28 + gst_18 + gst_12 
    d={"Name":name,"Room_No":room_num,"Folio_Num":folio_number[22:],"SAC_Code":sac_code,"Category":category,"Total_Invoice":total_invoice,"Total_amount":Total_amount,
    "Gst_28":gst_28,"Gst_18":gst_18,"Gst_12":gst_12,"Cess_amonut":Cess_amount,"Total_Tax":total_tax}
    return d
def main_fun(input_data):
    """Main function to separate 001: and 002: and remove unwanted data from that and
       and sort based on folio number and then separated folio number with each sac code
       and send that list to fun function and append the fun returned data to csv_data 
       variable and csv_data converted to dataframe and dataframe to excel file"""
    try:
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
            for i,y in enumerate(x):
                if re.search(r'-|1$',y[71:91]):
                    a = y[0:71]
                    b = "00000000000000000000"
                    rep=a+b
                    x[i] = rep
                if y[31:39] == "Paid Out":
                    a = y[0:71]
                    b = "00000000000000000000"
                    rep=a+b
                    x[i] = rep       
        total_data =[x for x in total_data if x!=[]]
        for x in total_data:
            if 'ZZZ ' in x[0][47:127]:
                for i,v in enumerate(x):
                    a = v[0:71]
                    b = "00000000000000000000"
                    rep=a+b
                    if i>=1:
                        x[i] = rep
        data_filtering = []
        for x in total_data:
            filtering_data = [ele for ele in x if ele not in unwanted_data]
            data_filtering.append(filtering_data)
        logger.info("FIltered some Unwanted Data") 
        dt = []
        for x in data_filtering:
            d = []
            li = []
            da = []
            for y in x: 
                d1 = []
                if re.search(r'^001:',y):
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
            if len(x) == 1:
                dup = x[0]
                x[0].append(' ')
                x[0].append('1234567')
                x[0].append(' ')    
                x[0].append(' ')
                x.insert(0,dup)    
        data_modifing1 = [ele for ele in dt if ele not in unwanted_data1]
        zzz_data = []
        data_modified = [ele for ele in data_modifing1 if ele not in zzz_data]
        column_names = ["Room_No", "First_Name", "Last_Name", "Folio_Num", "Tran_date","Code", "Description", "Amount"]
        tot_data = []
        for x in data_modified:
            if len(x) != 0:
                x.pop(0)
                for y in x:
                    assert4 = {k: v for k, v in zip(column_names, y)}
                    tot_data.append(assert4)
        for x in tot_data:
            v = x['Amount']
            vi = v[:10]+'.'+v[10:12]
            x['Amount'] = vi

        folio_nums=[]
        for x in tot_data:
            rr=x['Folio_Num']
            if rr not in folio_nums:
                folio_nums.append(rr)
            else:
                pass
        folio_nums.sort()  
        df = pd.DataFrame(tot_data)
        df_data=[]
        for x in folio_nums:
            df_A = df.loc[df['Folio_Num']== x]
            dit = df_A.to_dict("records")
            df_data.append(dit)
        logger.info("Sorted data based on folio number")
        main_list = []
        for record in df_data:
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
            Empty = []
            Remaining = []
            for x in record:
                co = x["Code"].strip(" ")
                if co in trans_codes['MiniBar_Chocolate']:
                    x["SAC_Code"] = "190532"
                    x["Category"] = "MiniBar_Chocolate"
                    MiniBar_Chocolate.append(x)
                elif co in trans_codes['MINIBAR_FOOD']:
                    x["SAC_Code"] = "210690"
                    x["Category"] = "MINIBAR_FOOD"
                    MINIBAR_FOOD.append(x)
                elif co in trans_codes['MiniBarSBev_Water']:
                    x["SAC_Code"] = "22029090"
                    x["Category"] = "MiniBar_SBev_Water"
                    MiniBarSBev_Water.append(x)    
                elif co in trans_codes['ACCOMODATION']:
                    x["SAC_Code"] = "996311"
                    x["Category"] = "ACCOMODATION"
                    ACCOMODATION.append(x)
                elif co in trans_codes['FOOD_SBEV']:
                    x["SAC_Code"] = "996332"
                    x["Category"] = "FOOD_SBEV"
                    FOOD_SBEV.append(x)
                elif co in trans_codes['BanquetsF_SB']:
                    x["SAC_Code"] = "996334"
                    x["Category"] = "Banquets_F_SB"
                    BanquetsF_SB.append(x)               
                elif co in trans_codes['TRANSPORT']:
                    x["SAC_Code"] = "996412"
                    x["Category"] = "TRANSPORT"
                    TRANSPORT.append(x)      
                elif co in trans_codes['LAUNDRY1']:
                    x["SAC_Code"] = "99712"
                    x["Category"] = "LAUNDRY1"
                    LAUNDRY1.append(x)
                elif co in trans_codes['BANQUET_HALLHIRE']:
                    x["SAC_Code"] = "997212"
                    x["Category"] = "BANQUET_HALLHIRE"
                    BANQUET_HALLHIRE.append(x)
                elif co in trans_codes['MISC_Banquets']:
                    x["SAC_Code"] = "997321"
                    x["Category"] = "MISC_Banquets"
                    MISC_Banquets.append(x)
                elif co in trans_codes['TELEPHONE']:
                    x["SAC_Code"] = "998412"
                    x["Category"] = "TELEPHONE"
                    TELEPHONE.append(x)
                elif co in trans_codes['WIFI']:
                    x["SAC_Code"] = "998422"
                    x["Category"] = "WIFI"
                    WIFI.append(x)
                elif co in trans_codes['TOBACCO']:
                    x["SAC_Code"] = "998819"
                    x["Category"] = "TOBACCO"
                    TOBACCO.append(x)
                elif co in trans_codes['Laundry']:
                    x["SAC_Code"] = "999712"
                    x["Category"] = "Laundry"
                    Laundry.append(x)
                elif co in trans_codes['HEALTHCLUB']:
                    x["SAC_Code"] = "999723"
                    x["Category"] = "HEALTHCLUB"
                    HEALTHCLUB.append(x)
                elif co in trans_codes['SPA']:
                    x["SAC_Code"] = "999799"
                    x["Category"] = "SPA" 
                    SPA.append(x)   
                else:
                    Remaining.append(x)
            main_list.append(MiniBar_Chocolate)
            main_list.append(MINIBAR_FOOD)
            main_list.append(ACCOMODATION)
            main_list.append(FOOD_SBEV)
            main_list.append(TRANSPORT)
            main_list.append(Laundry)
            main_list.append(MiniBarSBev_Water)
            main_list.append(BanquetsF_SB)
            main_list.append(LAUNDRY1)
            main_list.append(BANQUET_HALLHIRE)
            main_list.append(MISC_Banquets)
            main_list.append(TOBACCO)
            main_list.append(WIFI)
            main_list.append(TELEPHONE)
            main_list.append(HEALTHCLUB)
            main_list.append(SPA)
            main_list.append(Empty)
            main_list_2 = [x for x in main_list if x != []]
        csv_data = []
        for x in main_list_2:
            final_data = fun(x)
            csv_data.append(final_data)
        logger.info("Data is sorted based on folio number with each SAC code")    
        cc = pd.DataFrame(csv_data)
        logger.info("Data converted to panda DataFrame")
        cc.to_excel(os.getcwd()+"/"+file_name[0]+".xlsx", index=False,columns = ["Name","Room_No","Folio_Num","SAC_Code","Category","Total_Invoice","Total_amount","Gst_28","Gst_18","Gst_12","Cess_amonut","Total_Tax"])
        logger.info("Successfully Transfered  Data to excel file")
    except:
        logger.error(traceback.format_exc())


main_fun(input_data)