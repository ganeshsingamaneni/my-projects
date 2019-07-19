import re
import os
import sys
import logging 
import traceback
from itertools import groupby
import pandas as pd


 
  

def fun2(record,mylists,list_names,codes_list,trans_codes):
    ff = []
    non_codes={}
    list_names = list(list_names)
    for x in record:
        co = x["Code"].strip(" ")
        for i in range(len(list_names)):
            if co in trans_codes[list_names[i]]:
                sac_= trans_codes[list_names[i]]
                x["Category"] = list_names[i]
                x["Sac_code"] = sac_[-1]
                mylists[list_names[i]].append(x)
            else:
                if co not in codes_list:
                    non_codes[co]=x['Description']
    return mylists,non_codes            


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
        sac_code = x['Sac_code']
        category = x['Category']
        if "SGST" in x['Description']:
            if re.search(r'9',x['Description']):
                gst_per_number = '9'    
                amount = float(x['Amount'])
                Sgst_amount_9 += amount
            elif re.search(r'14',x['Description']):
                gst_per_number = '14'
                amount = float(x['Amount'])
                Sgst_amount_14 += amount
            elif re.search(r'6',x['Description']):
                gst_per_number = '6'
                amount = float(x['Amount'])
                Sgst_amount_6 += amount
            else:
                pass        
        elif "CGST" in x['Description']:
            description_in_x = x['Description']
            description = description_in_x[6:9]
            if re.search(r'9',x['Description']):
                amount = float(x['Amount'])

                Cgst_amount_9 += amount
            elif re.search(r'14',x['Description']):
                amount = float(x['Amount'])
                Cgst_amount_14 += amount
            elif re.search(r'6',x['Description']):
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
    d={"Name":name,"Room_No":room_num,"Folio_Num":folio_number[22:],"Category":category,"SAC_Code":sac_code,"Total_Invoice":total_invoice,"Total_amount":Total_amount,
    "Sgst_9%":Sgst_amount_9,"Cgst_9%":Cgst_amount_9,"Sgst_14%":Sgst_amount_14,"Cgst_14%":Cgst_amount_14,"Sgst_6%":Sgst_amount_6,"Cgst_6%":Cgst_amount_6,"Cess_amonut":Cess_amount,"Total_Tax":total_tax}
    
    return d

def main_fun(input_data,trans_codes,codes_list):
    """Main function to separate 001: and 002: and remove unwanted data from that and
       and sort based on folio number and then separated folio number with each sac code
       and send that list to fun function and append the fun returned data to csv_data 
       variable and csv_data converted to dataframe and dataframe to excel file"""
    try:
        modified_data = []
        codes_not_avaialbe={}
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
        # logger.info("FIltered some Unwanted Data") 
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

        for x in folio_nums:
            if x == "0000000000000000000000000000":
                folio_nums.remove(x)
        df = pd.DataFrame(tot_data)
        df_data=[]
        for x in folio_nums:
            df_A = df.loc[df['Folio_Num']== x]
            dit = df_A.to_dict("records")
            df_data.append(dit)
        # logger.info("Sorted data based on folio number")
        main_list = []
        list_names = trans_codes.keys()
        main_list=[]
        for record in df_data:
            my_lists = {key:[] for key in list_names}
            Remaining=[]
            dd,non = fun2(record,my_lists,list_names,codes_list,trans_codes)
            codes_not_avaialbe.update(non)
            
            for k,v in dd.items():
                if len(v)>0:
                    main_list.append(v)     
        main_list_2 = [x for x in main_list if x != []]
        csv_data = []
        for x in main_list_2:
            final_data = fun(x)
            # print(final_data)
            csv_data.append(final_data)
        # logger.info("Data is sorted based on folio number with each SAC code")    
        cc = pd.DataFrame(csv_data)
        # logger.info("Data converted to panda DataFrame")
        # cc.to_excel(os.getcwd()+"/"+file_name[0]+".xlsx", index=False,columns = ["Name","Room_No","Folio_Num","Category","SAC_Code","Total_Invoice","Total_amount","Sgst_9%","Cgst_9%","Sgst_14%","Cgst_14%","Sgst_6%","Cgst_6%","Cess_amonut","Total_Tax"])
        # logger.info("Successfully Transfered  Data to excel file")
        nnn = pd.DataFrame(codes_not_avaialbe.items(), columns=['Code', 'Description'])
        return cc,nnn,folio_nums
        # nnn.to_csv("/home/ganesh/Videos/no_codes/novotel_banglore.csv",index=False,columns=['Code','Description'])
    except Exception as e:
        # logger.exception("Exception Occured")
        return e


# main_fun(input_data)