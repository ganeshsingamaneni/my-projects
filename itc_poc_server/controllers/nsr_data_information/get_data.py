from datetime import datetime
from flask import make_response, request, send_file
from models.nsr_data_information import Nsr_Data_Information
from models.pm_master import Paper_Machine_Master
from models.product_master import Product_Master
from models.sales_category_master import Sales_Category_Master
from models.segment_master import Segment_Master
from models.profit_center_master import Profit_Center_Master
from schemas.pm_master_schema import PMMasterSchema
from schemas.product_master_schema import ProductMaster_Get_Schema
from schemas.sales_category_master_schema import Sales_Category_Master_Get_schema
from schemas.segment_master_schema import Segment_Master_Get_schema
from schemas.profit_center_master_schema import Profit_Center_Master_Get_schema
from schemas.nsr_data_information_schema import Nsr_Data_Information_Get_schema,Nsr_Data_2_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/nsr_data_information.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_nsr_data')
loggers = logging.getLogger("nsr_dataconsole")
import xlsxwriter
import string

class Get_Nsr_excel(Resource):
    def __init__(self):
        pass
    def get(self):
        try:
            nn  = list(string.ascii_letters[26:52])
            new_list = []
            for x in nn:
                new_list.append('A'+x) 
            third_list= []   
            for x in nn:
                third_list.append('B'+x)      
            a_z = nn + new_list
            workbook = xlsxwriter.Workbook(home+'/Nsr_data.xlsx')
            worksheet = workbook.add_worksheet()

            # Create a format to use in the merged range.
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'})
            merge_format2 = workbook.add_format({
                'bold': 2,
                'border': 1,
                'valign': 'vcenter'})    

            months_list = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']

            worksheet.merge_range('B1:C1', 'Machine Master', merge_format)
            worksheet.merge_range('D1:G1', 'Product Master', merge_format)
            worksheet.write('H1', 'Master', merge_format)
            worksheet.write('I1', 'Master ', merge_format)
            # worksheet.write('J1', 'Master ', merge_format)

            for x in a_z:
                if x == 'J':
                    ind = a_z.index(x)
            n = a_z[ind+len(months_list)-1]  
            worksheet.merge_range('J1:'+n+'1', 'Text Entry', merge_format)
            x1 = a_z.index(n)
            n1 = a_z[x1+1]
            worksheet.write(n1+'1', 'Auto Fill ', merge_format)
            x2 = a_z.index(n1)
            n2 = a_z[x2+1]
            n3 = a_z[x2+1+len(months_list)-1]

            worksheet.merge_range(n2+'1:'+n3+'1', 'Text Entry', merge_format)
            x3 = a_z.index(n3)
            n4 = a_z[x3+1]
            worksheet.write(n4+'1', 'Auto Fill ', merge_format)
            x4 = a_z.index(n4)
            n5 = a_z[x4+1]
            n6 = a_z[x4+1+len(months_list)-1]
            worksheet.merge_range(n5+'1:'+n6+'1', 'Auto Fill', merge_format)
            worksheet.write('B2', 'Machine Code', merge_format)
            worksheet.write('C2', 'Machine Name', merge_format)
            worksheet.write('D2', 'Product Short Des', merge_format)
            worksheet.write('E2', 'Profit Center', merge_format)
            worksheet.write('F2', 'Product Description', merge_format)
            worksheet.write('G2', 'Product Category', merge_format)
            worksheet.write('H2', 'Segment', merge_format)
            worksheet.write('I2', 'Sales Category', merge_format)
            # worksheet.write('J2', 'Prime/Stock Lot', merge_format)
            c = 0  
            for x in months_list:
                abc = a_z[ind+c]
                worksheet.write(abc+'2', 'Qty-'+x, merge_format)
                c+=1
            worksheet.write(a_z[ind+c]+'2', 'Qty-Total', merge_format)
            c+=1
            for x in months_list:
                abc = a_z[ind+c]
                worksheet.write(abc+'2', 'Nsr-'+x, merge_format)
                c+=1
            worksheet.write(a_z[ind+c]+'2', 'Nsr-Total', merge_format)
            c+=1
            for x in months_list:
                abc = a_z[ind+c]
                worksheet.write(abc+'2', 'Nsr value -'+x, merge_format)
                c+=1
            worksheet.write(a_z[ind+c]+'2', 'NSR Value Total', merge_format)
            categories = db.session.query(Nsr_Data_Information).order_by(Nsr_Data_Information.id).all()
            if categories:
                data_schema = Nsr_Data_Information_Get_schema(many=True)
                data = data_schema.dump(categories)
            req_keys =  ['paper_machine_id','product_id','profit_center_id','segment_id','sales_category_id','Qty_Apr','Qty_May','Qty_Jun','Qty_Jul','Qty_Aug','Qty_Sep','Qty_Oct','Qty_Nov','Qty_Dec','Qty_Jan','Qty_Feb','Qty_Mar','Qty_Total',
                        'NSR_Apr','NSR_May','NSR_Jun','NSR_Jul','NSR_Aug','NSR_Sep','NSR_Oct','NSR_Nov','NSR_Dec','NSR_Jan','NSR_Feb','NSR_Mar','NSR_Total','NSR_Value_Apr','NSR_Value_May','NSR_Value_Jun','NSR_Value_Jul','NSR_Value_Aug',
                        'NSR_Value_Sep','NSR_Value_Oct','NSR_Value_Nov','NSR_Value_Dec','NSR_Value_Jan','NSR_Value_Feb','NSR_Value_Mar','NSR_Value_Total']
            data_lists=[]
            for x in data:
                ll = []
                for ii in req_keys:
                    ll.append(x[ii])                    
                data_lists.append(ll)
            numb = 3    
            for x in data_lists:
                get_pm = db.session.query(Paper_Machine_Master).filter(
                Paper_Machine_Master.id == x[0]).first()
                if get_pm:
                    schema = PMMasterSchema()
                    paper_machine_data = schema.dump(get_pm)
                get_product = db.session.query(Product_Master).filter(
                Product_Master.id == x[1]).first()
                if get_product:
                    schema = ProductMaster_Get_Schema()
                    product_data = schema.dump(get_product)
                get_profit = db.session.query(Profit_Center_Master).filter(
                Profit_Center_Master.id == x[2]).first()
                if get_profit:
                    data_schema = Profit_Center_Master_Get_schema()
                    profit_data = data_schema.dump(get_profit)
                get_segment = db.session.query(Segment_Master).filter(
                Segment_Master.segment_code == x[3]).first()
                if get_segment:
                    data_schema = Segment_Master_Get_schema()
                    segment_data = data_schema.dump(get_segment) 
                get_sales = db.session.query(Sales_Category_Master).filter(
                Sales_Category_Master.sales_category_code == x[4]).first()

                if get_sales:
                    data_schema = Sales_Category_Master_Get_schema()
                    sales_data = data_schema.dump(get_sales)
                x.insert(0,paper_machine_data['paper_machine_code'])
                x.insert(1,paper_machine_data['paper_machine_name'])
                x.insert(2,product_data['product_short_description'])
                x.insert(3,profit_data['profit_code'])
                x.insert(4,product_data['product_description'])
                x.insert(5,product_data['category_product']['category_code'])
                x.insert(6,segment_data['segment_code'])
                x.insert(7,sales_data['sales_category_code'])
                x.insert(0,' ')
                del x[9:14]
                worksheet.write_row('A'+str(numb),tuple(x))
                numb+=1
                    


            numb+=3
            worksheet.merge_range('B'+str(numb)+':AA'+str(numb), 'Once Particular Machine ID is selected on sales screen, all PC mapped to that machine ID will auto populate.',merge_format2)
            worksheet.merge_range('B'+str(numb+1)+':AA'+str(numb+1), 'Once B3 is selected ,Column C to G should auto populate',merge_format2)
            worksheet.merge_range('B'+str(numb+2)+':AA'+str(numb+2),'Output Reqd',merge_format2)
            worksheet.merge_range('B'+str(numb+3)+':AA'+str(numb+3),'Machines Wise & Grade Wise Sales Qty,NSR,NSR Value',merge_format2)
            worksheet.merge_range('B'+str(numb+4)+':AA'+str(numb+4),'Machines Wise & Segment Wise Sales Qty,NSR,NSR Value',merge_format2)
            worksheet.merge_range('B'+str(numb+5)+':AA'+str(numb+5),'Machines Wise & sales category Wise Sales Qty,NSR,NSR Value',merge_format2)
            worksheet.merge_range('B'+str(numb+6)+':AA'+str(numb+6),'Machines Wise & Prime/Stock Lot Wise Sales Qty,NSR,NSR Value',merge_format2)
            worksheet.merge_range('B'+str(numb+7)+':AA'+str(numb+7),'any other combination of same',merge_format2)
            workbook.close()
            logger.info("succesfully created excel file in required path")
            return send_file(home+'/Nsr_data.xlsx', as_attachment=True)
            # return({"success":True,"data":"data"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})    

