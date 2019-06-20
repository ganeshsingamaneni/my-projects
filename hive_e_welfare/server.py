from flask import Flask
from config import *

app = Flask(__name__)
from models.hive_config import connect
from config import *
import datetime
from flask import jsonify
from models.sql.schedularlogs import Transpayment
s = connect()

@app.route("/home")
def func():
    final_data=[]
    c ={}
    sub=[]
    d = {}
    e = {}
    column_name_list = []
    unique_listof_bank_account_no = []
    list_of_bank_accout_no = []
    total_data_ofa_table = []
    personal_num_list=[]
    query1 = 'SHOW COLUMNS from src_transpaymentfact'
    column_name_execution = s.execute(query1)
    column_names_data = list(column_name_execution)
    for column_names in column_names_data:
        column=column_names[0]
        column_name_list.append(column)
    query2 = 'select * from src_transpaymentfact limit 10000'
    query_object = s.execute(query2)
    table_total_data = list(query_object)
    for x in table_total_data:
        data = dict(zip(column_name_list,x))
        b = data["trans_payment_fact_bank_account_no"]
        total_data_ofa_table.append(data)
        list_of_bank_accout_no.append(b)
    for con in list_of_bank_accout_no:
        if con not in d:
            d[con]=1
        else:
            d[con] +=1
    duplicate_bank_account_no = {k:v for (k,v) in d.items() if v > 1}
    unique_listof_bank_account_no_withdata = list({v['trans_payment_fact_bank_account_no']:v for v in total_data_ofa_table}.values())
    #print("........: ",len(unique_listof_bank_account_no_withdata))
    for x in unique_listof_bank_account_no_withdata:
        unique_listof_bank_account_no.append(x['trans_payment_fact_bank_account_no'])
    for x in unique_listof_bank_account_no_withdata:
        personal_num_list.append(x['trans_payment_fact_bank_personal_no'])
    for con in personal_num_list:
        if con not in d:
            d[con]=1
        else:
            d[con] +=1
    duplicate_bank_personal_no = {k:v for (k,v) in d.items() if v > 1}
    #print("//: ",duplicate_bank_personal_no)
    unique_listof_bank_personal_no_withdata = list({v['trans_payment_fact_bank_personal_no']:v for v in unique_listof_bank_account_no_withdata}.values())
    for d in unique_listof_bank_account_no_withdata:
        c.setdefault(d['trans_payment_fact_bank_personal_no'], []).append(d['uniqnumber'])
    b = [{k: v} for k,v in c.items()]
    for x in b:
       unique = {k:v for (k,v) in x.items() if len(v)>1}
       sub.append(unique)
    unique_numbers = [i for i in sub if i]
    print(unique_numbers)
    for key in unique_numbers:
        for a,b in key.items():
            for  i in a:
                for t in total_data_ofa_table:
                    for k,v in t.items():
                        if v == i:
                            account_no = t['trans_payment_fact_bank_account_no']
                            personal_no = t['trans_payment_fact_bank_personal_no']
                            count_account_no = 0
                            count_personal_no = 0
                            for x,y in duplicate_bank_account_no.items():
                                 if account_no == x:
                                     count_account_no = y
                                     for x,y in duplicate_bank_personal_no.items():
                                         if personal_no == x:
                                             count_personal_no = y
                                     ref_numbers = b
                                     total_data = {"account_no":account_no,"personal_no":personal_no,"count_account_no":count_account_no,"count_personal_no":count_personal_no,"ref_number":ref_numbers}
                                     final_data.append(total_data)
                                     print("TTT: ",total_data)
    return "ok"

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)
