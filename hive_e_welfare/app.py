from flask import Flask
from config import *

app = Flask(__name__)
from models.hive_config import connect
from config import *
import datetime
from flask import jsonify
from models.sql.schedularlogs import Transpayment
s = connect()

@app.route("/home1")
def func():
    d = {}
    e = {}
    column_name_list = []
    list_of_bank_accout_no = []
    total_data_ofa_table = []
    bank_personal_no_list =[]
    duplicate_account_no_with_data=[]
    personal_num_of_duplicate_account_with_data=[]
    personal_num_list=[]
    query1 = 'SHOW COLUMNS from src_transpaymentfact'
    column_name_execution = s.execute(query1)
    column_names_data = list(column_name_execution)
    for column_names in column_names_data:
        column=column_names[0]
        column_name_list.append(column)
    query2 = 'select * from src_transpaymentfact limit 40000'
    query_object = s.execute(query2)
    table_total_data = list(query_object)
    for x in table_total_data:
        data = dict(zip(column_name_list,x))
        b = data["trans_payment_fact_bank_account_no"]
        total_data_ofa_table.append(data)
        list_of_bank_accout_no.append(b)
    #print("/....: ",total_data_ofa_table)
    #print(",,,,,,,,,: ",list_of_bank_accout_no)
    for con in list_of_bank_accout_no:
        if con not in d:
            d[con]=1
        else:
            d[con] +=1
    duplicate_bank_account_no = {k:v for (k,v) in d.items() if v > 1}
    #print("//: ",duplicate_bank_account_no)
    unique_listof_bank_account_no = list({v['trans_payment_fact_bank_account_no']:v for v in total_data_ofa_table}.values())
    #print("........: ",len(unique_listof_bank_account_no))
    for l in unique_listof_bank_account_no:
        bank_personal_no_list.append(l['trans_payment_fact_bank_personal_no'])
    for con in bank_personal_no_list:
        if con not in e:
            e[con]=1
        else:
            e[con] +=1
    duplicate_values_bank_personal_no = {k:v for (k,v) in e.items() if v > 1}
    #print("[[[[[[[]]]]]]]: ",duplicate_values_bank_personal_no)
    unique_listof_bank_personal_no = list({v['trans_payment_fact_bank_personal_no']:v for v in unique_listof_bank_account_no}.values())
    #print("aaaaaaaa: ",unique_listof_bank_personal_no)
    for k in duplicate_bank_account_no.keys():
        a = list(filter(lambda total_data_ofa_table: total_data_ofa_table['trans_payment_fact_bank_account_no'] == k, total_data_ofa_table))
        #print("///// :",a)
        duplicate_account_no_with_data.append(a)
        for x in duplicate_account_no_with_data:
            personal_num_of_duplicate_account_with_data.append(x)
        #print("]]]]]]]: ",personal_num_of_duplicate_account_with_data)
        for val in personal_num_of_duplicate_account_with_data:
            #print("mmmmmm: ",val)
            for val2 in val:
                z=val2['trans_payment_fact_bank_personal_no']
                personal_num_list.append(z)
    #print("]]]]: ",len(duplicate_account_no_with_data))
    for k in personal_num_list:
        #print("//////: ",k)
        a = list(filter(lambda duplicate_account_no_with_data: duplicate_account_no_with_data['trans_payment_fact_bank_personal_no'] == k, duplicate_account_no_with_data))
        print("ggggg: ",a)
        break
    return 'ok'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)
