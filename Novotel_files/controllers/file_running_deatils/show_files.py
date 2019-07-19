from flask import make_response,request,send_file
from flask_restful import Api, Resource
import logging, logging.config, yaml
from urllib.parse import urlparse
import re,pathlib
import os,json
import sys,pathlib
import pandas as pd
from os.path import expanduser
home = expanduser("~")
from datetime import date



class File_display_excel(Resource):
    def __init__(self):
        pass

    def get(self,par_date):
        try:
            with open(home+"/config.json") as f:
                    file_path = json.load(f)
            files_by_date = os.listdir(file_path["Output_files_path"]+par_date)
            print(files_by_date)
            for x in files_by_date:
                if x.endswith(".xlsx"):
                    return_path =file_path["Output_files_path"]+par_date+"/"+x    
            return ({"Success":True,"download_link":return_path})

        except Exception as e:
            return ({"Success":False,"Message":str(e)})



class File_display_csv(Resource):
    def __init__(self):
        pass

    def get(self,par_date):
        try:
            with open(home+"/config.json") as f:
                    file_path = json.load(f)
            files_by_date = os.listdir(file_path["Output_files_path"]+par_date)
            print(files_by_date)
            for x in files_by_date:
                if x.endswith(".csv"):
                    return_path =file_path["Output_files_path"]+par_date+"/"+x    
            return ({"Success":True,"download_link":return_path})

        except Exception as e:
            return ({"Success":False,"Message":str(e)})
                