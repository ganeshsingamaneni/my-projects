from datetime import datetime
from flask import make_response,request,send_file
from models.file_model import Output_files_Details
from os.path import expanduser
home = expanduser("~")
# print(home)
# from home import config
from models.hotel_model import Hotel_Details
from schemas.hotel_schema import Hotel_Details_Schema
from models.sac_code_model import Sac_Tran_Codes_Mapping
from schemas.file_schema import Output_Files_Schema
from schemas.sac_code_schema import Sac_code_Schema
from config import *
from flask_restful import Api, Resource
from sqlalchemy import create_engine
from controllers.parsing import main_fun
import logging, logging.config, yaml
import re,pathlib
import os,json
import sys
import pandas as pd

from datetime import date

CONFIG_PATH = os.path.join(basedir,'loggeryaml/filelogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('postfile')
loggers = logging.getLogger("fileconsole")

today = date.today()
today_date = today.strftime("%d-%m-%Y")


class File_Details(Resource):
    def __init__(self):
        pass

    # output files  details get call
    def get(self):
        try:
            sac_code=db.session.query(Output_files_Details).order_by(Output_files_Details.id).all()
            if sac_code:
                data_schema = Output_Files_Schema(many=True)
                data = data_schema.dump(sac_code).data
                logger.info("getting data of output file details is success")
                return ({"Success":True,"message":data})
            return({"Success":False,"message":"no data is available on Hotels"})
        except Exception as e:
            logger.exception("get data of output file details is Failed")
            return ({"Success":False,"message":str(e)})

    def post(self):
        try:
            try:
                with open(home+"/config.json") as f:
                    file_path = json.load(f)
                os.makedirs(file_path["Output_files_path"])
            except FileExistsError:
                pass
            sac_code=db.session.query(Sac_Tran_Codes_Mapping).order_by(Sac_Tran_Codes_Mapping.id).all()
            if sac_code:
                data_schema = Sac_code_Schema(many=True)
                data = data_schema.dump(sac_code).data
            hotel_details = db.session.query(Hotel_Details).order_by(Hotel_Details.id).all()
            if hotel_details:
                data_schema = Hotel_Details_Schema(many=True)
                hotel_data = data_schema.dump(hotel_details).data
            trans_codes = {}
            for x in data:
                key = x['descrption_name']
                value = x['tran_codes']
                next_value = x['sac_code']
                comb = lambda s,n: [s[i:i+n] for i in range(0,len(s),n)]
                dict_value = comb(value,4)
                dict_value.append(next_value)
                dict_={key:dict_value}
                trans_codes.update(dict_)
            codes_list=[]
            for x,y in trans_codes.items():
                codes_list.extend(y)
            files = request.files['file']
            upload_folder = os.path.basename('/upload')
            f = os.path.join(upload_folder, files.filename)
            files.save(f)
            Input = open(f,'r')
            head, tail = os.path.split(f)
            file_name = tail.split(".")
            input_data = Input.readlines()
            vv,vvv,folio_numbers = main_fun(input_data,trans_codes,codes_list)
            latest_folio=[]
            for x in folio_numbers:
                latest_folio.append(x[22:])
            folio_start=latest_folio[0]
            folio_end = latest_folio[-1]
            if len(vv) >0:
                try:
                    os.makedirs(file_path["Output_files_path"]+today_date)
                except FileExistsError:
                    pass
                vv.to_excel(file_path["Output_files_path"]+"/"+today_date+"/"+file_name[0]+".xlsx", index=False,columns = ["Name","Room_No","Folio_Num","Category","SAC_Code","Total_Invoice","Total_amount","Sgst_9%","Cgst_9%","Sgst_14%","Cgst_14%","Sgst_6%","Cgst_6%","Cess_amonut","Total_Tax"])
                logger.info("generating output excel file is success")
                vvv.to_csv(file_path["Output_files_path"]+"/"+today_date+"/"+file_name[0]+"_No_Codes.csv",index=False,columns=['Code','Description'])
                logger.info("generating no codes csv  file is success")
                file1=file_path["Output_files_path"]+"/"+today_date+"/"+file_name[0]+".xlsx"
                file2=file_path["Output_files_path"]+"/"+today_date+"/"+file_name[0]+"_No_Codes.csv"
                Mail_index("Output Files",hotel_data[0]['email'],"hii bhanu chander",file1,file2)
                logger.info("sending mail is success")
                db_dit = {"job_done":True,"folio_starting_number":folio_start,"folio_ending_number":folio_end,"file_name":file_name[0]}
                schema = Output_Files_Schema()
                new_code = schema.load(db_dit, session=db.session).data
                db.session.add(new_code)
                db.session.commit()
                data = schema.dump(new_code).data
                logger.info("job done is success and returned no codes csv file")
            else:
                db_dit = {"job_done":False,"folio_starting_number":folio_start,"folio_ending_number":folio_end,"file_name":file_name[0]}
                schema = Output_Files_Schema()
                new_code = schema.load(db_dit, session=db.session).data
                db.session.add(new_code)
                db.session.commit()
                data = schema.dump(new_code).data
                logger.info("job done is fasle")
            os.remove(cwd+"/"+f)    
            return ({"Success":True,"message":data})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"Success":False,"message":str(e)})


class Data_between_dates(Resource):
    def __init__(self):
        pass
    def get(self,start,end):
        print(start,end)
        try:
            sac_code=db.session.query(Output_files_Details).filter(Output_files_Details.last_run_time.between(start,end))
            if sac_code:
                data_schema = Output_Files_Schema(many=True)
                data = data_schema.dump(sac_code).data
                logger.info("getting data of output file details is success")
                return ({"success":True,"message":data})
            return({"success":False,"message":"no data is available on Hotels"})
        except Exception as e:
            logger.error("get data of output file details is Failed")
            return ({"success":False,"message":str(e)})

