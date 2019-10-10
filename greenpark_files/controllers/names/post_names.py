from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from models.names_model import Outlet_Details
from schemas.namesschema import Names_Schema,Names_Get_Schema
import pandas as pd
from flask import make_response, Flask, request
from config import *
from sqlalchemy import create_engine
import sqlalchemy,datetime
import json
import sys
import logging
import logging.config
# import yaml
import os
import logging
from os.path import expanduser
home = expanduser("~")
# CONFIG_PATH = os.path.join(basedir, 'loggeryaml/sac_codes.yaml')
# logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
# logger = logging.getLogger('postsac_codes_data')
# loggers = logging.getLogger("sac_code_dataconsole")


class Post_Outlets(Resource):
    ''' This call is to add new hotel sac codes mapped Transaction codes and to get all the hotels sac code mapped tran codes '''

    def __init__(self):
        pass

    def get(self):
        ''' This method is to get  all the hotels sac code mapped tran codes  '''
        try:
            saccodes = db.session.query(Outlet_Details).all()
            if saccodes:
                schema = Names_Schema(many=True)
                data = schema.dump(saccodes)
                # logger.info("Sac code mapping Data feteched successfully")
                # loggers.info("Sac code mapping Data feteched successfully")
                return ({"success": True, "data": data})
            else:
                # logger.warning("No data is available for Sac code mapping")
                # loggers.info("No data is available for Sac code mapping")
                return({"success": False, "message": "No data is available for sac_codes"})
        except Exception as e:
            # logger.exception("Exception occured")
            return({"success": False, "message": str(e)})

    def post(self):
        '''This method is to add the new hotel sac code mapped tran codes '''
        try:
            da = request.get_json()
            name = da['Outlet_Name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Outlet_Details).filter(
                Outlet_Details.Outlet_Name == name).one_or_none()
            if existing_one is None:
                schema = Names_Schema()
                new_hotel = schema.load(dit, session=db.session)
                db.session.add(new_hotel)
                db.session.commit()
                new_sechema = Names_Schema
                new = db.session.query(Outlet_Details).filter(
                Outlet_Details.Outlet_Name == name).all()
                new_sechema = Names_Schema(many=True)
                data = new_sechema.dump(new)
                # logger.info("Hotel Details posted succesfully")
                # loggers.info("Hotel Details posted succesfully")
                return ({"success": True, "message": data})
            else:
                return ({"success": False, "message": "hotel account already exists"})
        except Exception as e:
            # logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})