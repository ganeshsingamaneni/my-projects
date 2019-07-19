from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from schemas.sac_code_schema import Sac_code_Schema
import pandas as pd
from flask import make_response,Flask,request
from config import *
from sqlalchemy import create_engine
import sqlalchemy
import json,sys
import logging, logging.config, yaml
import os,logging
from os.path import expanduser
home = expanduser("~")
CONFIG_PATH = os.path.join(basedir,'loggeryaml/saclogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('postsaccode')
loggers = logging.getLogger("consolepostsaccode")


class Post_Sac_Codes(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            saccodes=db.session.query(Sac_Tran_Codes_Mapping).all()
            if saccodes:
                schema      = Sac_code_Schema(many=True)
                data        = schema.dump(saccodes).data
                logger.info("Sac code mapping Data feteched successfully")
                return ({"success":True,"data":data})
            else:
                logger.warning("No data is available for Sac code mapping")
                return({"success":False,"message":"No data is available for sac_codes"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})

    def post(self):
        try:
            try:
                name = request.get_json()
                name = name['name']
                if name == "Hyderabad_airport":
                    with open(home+"/my-projects/Novotel_files/nov_air.json") as datafile:
                        no_air_codes  = json.load(datafile)
                elif name == "Hyderabad_convention":
                    with open(home+"/my-projects/Novotel_files/nov_conv.json") as datafile:
                        no_air_codes  = json.load(datafile)
                elif name == "Banglore":
                    with open(home+"/my-projects/Novotel_files/nov_bang.json") as datafile:
                        no_air_codes  = json.load(datafile)
            except Exception as e:
                return({"success":False,"message":str(e)})                

            description=[]
            S_code =[]
            Tran_codes=[]
            for key,value in no_air_codes.items():
                description.append(key)
                str1 = ''.join(str(e) for e in value[:-1])
                S_code.append(value[-1])
                Tran_codes.append(str1)
            df = pd.DataFrame({"descrption_name":description,
                                "sac_code":S_code,
                                "tran_codes":Tran_codes})
            dit = df.to_dict("records")
            for x in dit:
                schema = Sac_code_Schema()
                new_code = schema.load(x, session=db.session).data
                db.session.add(new_code)
                db.session.commit()
                data = schema.dump(new_code).data
            logger.info("Sac code mapping data posted succesfully")
            return ({"Success":True,"message":"data"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})
