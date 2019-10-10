from datetime import datetime
from flask import make_response, request, send_file
from models.nsr_data_information import Nsr_Data_Information
from models.pm_master import Paper_Machine_Master
from models.product_master import Product_Master
from models.profit_center_master import Profit_Center_Master
from models.sales_category_master import Sales_Category_Master
from schemas.product_master_schema import ProductMaster_Get_Schema
from schemas.pm_master_schema import PMMasterSchema
from schemas.profit_center_master_schema import Profit_Center_Master_Get_schema
from schemas.category_master_schema import Category_Master_Get_schema
from schemas.sales_category_master_schema import Sales_Category_Master_Get_schema
from schemas.machine_production_data_information_schema import Machine_Production_Data_Information_Get_schema
from config import *
from sqlalchemy import and_, or_, not_
from flask_restful import Api, Resource
import os
from os.path import expanduser
import datetime
import logging
import logging
import logging.config
import yaml
home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/time_balancing.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_time_balancing')
loggers = logging.getLogger("time_balancing_console")
import xlsxwriter
import string

class Get_time_balancing_output_excel(Resource):
    def __init__(self):
        pass
    def post(self):
        try:
       
            workbook = xlsxwriter.Workbook(home+'/output_time_balancing.xlsx')
            worksheet = workbook.add_worksheet()



            # Create a format to use in the merged range.
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'})
            merge_format2 = workbook.add_format({
                'bold': 1,
                'border': 1,
                'valign': 'vcenter'})    
          

            worksheet.merge_range('B1:C1', 'Machine Master', merge_format)
            worksheet.merge_range('D1:G1', 'Product Master', merge_format)
            worksheet.write('H1', 'Master', merge_format)
            worksheet.write('I1', 'Master', merge_format)
            worksheet.write('J1', 'Auto populate from Sales Master', merge_format)
            worksheet.write('K1', 'Auto populate from Input Master', merge_format)

            worksheet.write('B2', 'Machine Name', merge_format)
            worksheet.write('C2', 'Machine Name', merge_format)
            worksheet.write('D2', 'Product Short Des', merge_format)
            worksheet.write('E2', 'Profit Center', merge_format)
            worksheet.write('F2', 'Product Description', merge_format)
            worksheet.write('G2', 'Product Category', merge_format)
            worksheet.write('H2', 'Segment', merge_format)
            worksheet.write('I2', 'Sales Category', merge_format)
            worksheet.write('J2', 'Qty-Total', merge_format)
            worksheet.write('K2', 'Days Required for Saleable Production', merge_format)
            
            da = request.get_json()
            
            # da = {"data":[{"machine_code":1212,"machine_name":"2ddd",'segment_id': 1,"sales_category_id":2,"Qty_Total":3,"days_required": 2,"product_short_description":'cs',"profit_code": "vfvs","product_description":'fsrg',"category_name":"Vsdvsd"},
            # {"machine_code":1212,"machine_name":"2ddd",'segment_id': 1,"sales_category_id":2,"Qty_Total":3,"days_required": 2,"product_short_description":'cs',"profit_code": "vfvs","product_description":'fsrg',"category_name":"Vsdvsd"},
            # {"machine_code":1212,"machine_name":"2ddd",'segment_id': 1,"sales_category_id":2,"Qty_Total":3,"days_required": 2,"product_short_description":'cs',"profit_code": "vfvs","product_description":'fsrg',"category_name":"Vsdvsd"}]}
            dit = {key: value for key, value in da.items()}
            values = dit['data']
            data_lists=[]
            for x in values:
                ll = []
                ll.append(x['machine_code'])
                ll.append(x['machine_name'])
                ll.append(x['product_short_description'])
                ll.append(x['profit_code'])
                ll.append(x['product_description'])
                ll.append(x['category_name'])
                ll.append(x['segment_id'])
                ll.append(x['sales_category_id'])
                ll.append(x['Qty_Total'])
                ll.append(x['days_required'])
                data_lists.append(ll)  
            numb = 3     
            for x in data_lists:
                x.insert(0,' ')

                worksheet.write_row('A'+str(numb),tuple(x))
                numb+=1
            worksheet.write('J'+str(numb), 'sum(3:10)', merge_format)
            numb+=1
            extra = [['Days Required','sum(3:10)',' ','A'],['Days Available','365/366','Based on Year','B'],['Days Required<=Days Available','Check',' ','C'],
                    ['Down Time Days','Auto Fill','B-A','D'],['Down Time %','Auto Fill','D/B','E'],['Down Time % As per Input Master','Auto Fill from Input master for PM1A',' ','F']]
            numb+=2
            for each in extra:
                worksheet.write_row('K'+str(numb),tuple(each))
                numb+=1
            numb+=1    
            worksheet.write('K'+str(numb), 'Condition', merge_format)
            an_extra = [['If E=F','Machine Balancing Ok','Check'],['If E>F','Either Reduce Production or increase Sales','Check'],
                        ['If E<F','Either increase Production or reduce Sales','Check']]


            numb+=1
            worksheet.merge_range('B'+str(numb)+':I'+str(numb), ' Time/Machine Balancing has to be done machine wise and in total for FY (not required month wise)', merge_format2)
            worksheet.merge_range('B'+str(numb+1)+':I'+str(numb+1), ' Time/Machine Balancing has to be done by Finance Team', merge_format2)
            worksheet.merge_range('B'+str(numb+2)+':I'+str(numb+2), ' Time/Machine Balancing has to be done after input master Screen is locked', merge_format2)

            for each in an_extra:
                worksheet.write_row('K'+str(numb),tuple(each))
                numb+=1            

            workbook.close()
            logger.info("succesfully created excel file in required path")
            return send_file(home+'/output_time_balancing.xlsx', as_attachment=True)
            # return({"success":True,"data":"data"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})    

