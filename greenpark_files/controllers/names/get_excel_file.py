from datetime import date, timedelta
import datetime
from sqlalchemy import and_, func, extract
import os
# import logging.config
import pandas as pd
import sys
from controllers.parsing import main_func
from sqlalchemy import create_engine
from flask_restful import Api, Resource
from config import *
from models.names_model import Outlet_Details
from schemas.namesschema import Names_Get_Schema, Names_Schema
from models.file_details import Files_Details
from schemas.filedetailsschema import Files_Details_Schema

class File_Details_To_Excel(Resource):
    def __init__(self):
        pass

    # output files  details get call
    def get(self):
        try:
            sac_code = db.session.query(Files_Details).order_by(
                Files_Details.id).all()
            if sac_code:
                data_schema = Files_Details_Schema(many=True)
                data = data_schema.dump(sac_code)
                # logger.info("getting data of output file details is success")
                return ({"success": True, "message": data})
            return({"success": False, "message": "no data is available"})
        except Exception as e:
            # logger.exception("get data of output file details is Failed")
            return ({"success": False, "message": str(e)})