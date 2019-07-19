from config_hive import conn
from datetime import datetime
from flask import make_response,request
from models.trans_payment_rule1model import Transpayment_fact_rule1
from flask_restful import Api, Resource
from schemas.rule1_schema import Rule1_Schema
import pandas as pd
import datetime

from config import db
import json
class Post_Transfact_details(Resource):
    def __init__(self):
        pass

    def post(self):
        # try:
        start = datetime.datetime.utcnow()
        print(start)
        df = pd.read_sql("select * from src_transpaymentfact limit 1000",conn)
        print(datetime.datetime.utcnow(),df.shape)
        group = df.groupby('src_transpaymentfact.trans_payment_fact_bank_account_no')['src_transpaymentfact.trans_payment_fact_personal_name'].count()
        dit = group.to_dict()
        dup_accounts=[]
        for x,y in dit.items():
            if y > 0:
                dup_accounts.append(x)
        new_list=[]
        for x in dup_accounts:
            v= df.loc[df['src_transpaymentfact.trans_payment_fact_bank_account_no'] == x]
            v = v[['src_transpaymentfact.trans_payment_fact_bank_account_no','src_transpaymentfact.trans_payment_fact_personal_name','src_transpaymentfact.trans_payment_fact_amount','src_transpaymentfact.trans_payment_fact_person_id','src_transpaymentfact.uniqnumber']]
            uniq_num =v['src_transpaymentfact.uniqnumber'].tolist()
            amount = v['src_transpaymentfact.trans_payment_fact_amount'].tolist()
            account_num = v['src_transpaymentfact.trans_payment_fact_bank_account_no'].tolist()
            di = v.to_dict("records")
            last_dict = {"amount":str(amount[0]),"bank_account_no":account_num[0],
                "receipt_count":len(uniq_num),"ref":{"data":uniq_num}}
            new_list.append(last_dict)
        print(len(new_list))    
        for x in new_list:
            new_list = Transpayment_fact_rule1(
                amount=x['amount'],
                bank_account_no=x['bank_account_no'],
                receipt_count=str(x['receipt_count']),
                ref=x['ref'])
            db.session.add(new_list)
            db.session.commit()
        end = datetime.datetime.utcnow()
        print(end)    
        return ({"Success":True,"start":start,"end":end})
        # except Exception as e:
        #     return ({"success":False,"message":str(e)})    
