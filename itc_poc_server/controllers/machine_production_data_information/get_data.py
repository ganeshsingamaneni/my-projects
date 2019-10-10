from datetime import datetime
from flask import make_response, request, send_file
from models.machine_production_data_information import Machine_Production_Data_Information
from models.pm_master import Paper_Machine_Master
from models.product_master import Product_Master
from models.profit_center_master import Profit_Center_Master
from models.category_master import Category_Master
from schemas.product_master_schema import ProductMaster_Get_Schema
from schemas.pm_master_schema import PMMasterSchema
from schemas.profit_center_master_schema import Profit_Center_Master_Get_schema
from schemas.category_master_schema import Category_Master_Get_schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/machine_product_data_information.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postmachine_product_data')
loggers = logging.getLogger("machine_product_dataconsole")
import xlsxwriter
import string

class Get_Machine_Production_excel(Resource):
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
            a_z = nn + new_list + third_list
            
            # Create an new Excel file and add a worksheet. machine_production_data
            workbook = xlsxwriter.Workbook(home+'/machine_production_data.xlsx')
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
            merge_format3 = workbook.add_format({
                'bold': 1,
                'border': 4,
                'valign': 'vcenter'})
            months_list = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']

            worksheet.merge_range('B1:C1', 'Machine Master', merge_format)
            worksheet.merge_range('D1:G1', 'Product Master', merge_format)
            for x in a_z:
                if x == 'H':
                    ind = a_z.index(x)
            n = a_z[ind+len(months_list)]  
            worksheet.merge_range('H1:'+n+'1', 'Auto populate from Sales Master', merge_format)
            x1 = a_z.index(n)
            n1 = a_z[x1+1]
            n2 = a_z[x1+4]
            worksheet.merge_range(n1+'1:'+n2+'1', 'Text Entry', merge_format)
            x2 = a_z.index(n2)
            n3 = a_z[x2+1]
            worksheet.write(n3+'1', 'Autofill ', merge_format)
            x3 = a_z.index(n3)
            n4 = a_z[x3+1]
            n5 = a_z[x3+8]
            worksheet.merge_range(n4+'1:'+n5+'1', 'Text Entry', merge_format)
            x4 = a_z.index(n5)
            n6 = a_z[x4+1]
            n7 = a_z[x4+18]
            worksheet.merge_range(n6+'1:'+n7+'1', 'Auto Fill', merge_format)

            x5 = a_z.index(n7)
            n8 = a_z[x5+1]
            n9 = a_z[x5+6]
            worksheet.merge_range(n8+'1:'+n9+'1', 'Auto Fill', merge_format)
            worksheet.write('B2', 'Machine Name', merge_format)
            worksheet.write('C2', 'Machine Name', merge_format)
            worksheet.write('D2', 'Product Short Des', merge_format)
            worksheet.write('E2', 'Profit Center', merge_format)
            worksheet.write('F2', 'Product Description', merge_format)
            worksheet.write('G2', 'Product Category', merge_format)
            c = 0  
            for x in months_list:
                abc = a_z[ind+c]
                worksheet.write(abc+'2', 'Qty-'+x, merge_format)
                c+=1
            worksheet.write(a_z[ind+c]+'2', 'Qty-Total', merge_format)
            c+=1


            keys_list=['Reel %','Sheet %-ISS','Sheet %-OSS','TPH','Machine Hr/Ton','C&W%-Reel','C&W%-ISS','C&W%-OSS','FL%-Reel','FL%-ISS','FL%-OSS',
                        'Replup %','Down Time %','Reel- Qty','Sheet-ISS Qty','Sheet-OSS Qty','C&W Qty-Reel','C&W Qty-ISS','C&W Qty-OSS','C&W Qty-Total',
                        'Naked-Reel Qty','Naked-Sheet ISS Qty','Naked-Sheet OSS Qty','Naked Production','FL Qty-Reel','FL Qty-ISS','FL Qty-OSS','FL Qty-Total',
                        'Machine Production-Total','Conv Factor','Gross TPD','Net TPD','Naked TPD','Saleable TPD','Days Required']
            for x in keys_list:
                worksheet.write(a_z[ind+c]+'2', x, merge_format)
                c+=1
            categories = db.session.query(Machine_Production_Data_Information).order_by(Machine_Production_Data_Information.id).all()
            if categories:
                data_schema = Machine_Production_Data_Information_Get_schema(many=True)
                data = data_schema.dump(categories)
            req_keys =  ['paper_machine_id',"product_id", "profit_center_id", "category_master_id", "Qty_Apr", "Qty_May", "Qty_Jun", 
                        "Qty_Jul", "Qty_Aug", "Qty_Sep", "Qty_Oct", "Qty_Nov", "Qty_Dec", "Qty_Jan", "Qty_Feb", "Qty_Mar", "Qty_Total", "reel_percentage", "sheet_ISS_percentage",
                        "sheet_OSS_percentage", "TPH_total", "machine_hr_ton", "CW_percentage_Reel", "CW_percentage_ISS", "CW_percentage_OSS", "CW_percentage_FL_reel", "CW_percentage_FL_ISS",
                        "CW_percentage_FL_OSS", "repulp_percentage", "down_time_percentage", "reel_qty", "sheet_ISS_qty", "sheet_OSS_qty", "cw_qty_reel", "cw_qty_ISS", "cw_qty_OSS", "cw_qty_total", "naked_reel_qty", "naked_sheet_ISS_qty", "naked_sheet_OSS_qty", "naked_production", "FL_qty_reel", "FL_qty_ISS", "FL_qty_OSS", "FL_qty_total", "machine_production_total",
                        "conv_factor", "gross_TPD", "net_TPD", "naked_TPD", "saleable_TPD", "days_required"]
            data_lists=[]
            for x in data:
                ll = []
                for ii in req_keys:
                    ll.append(x[ii])                    
                data_lists.append(ll)  
            numb = 3     
            for x in data_lists:

                get_pm = db.session.query(Paper_Machine_Master).filter(Paper_Machine_Master.id == x[0]).first()
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
                # get_category = db.session.query(Category_Master).filter(
                #     Category_Master.id == x[3]).first()
                # if get_category:
                #     data_schema = Category_Master_Get_schema()
                #     segment_data = data_schema.dump(get_category) 
                x.insert(0,paper_machine_data['paper_machine_code'])
                x.insert(1,paper_machine_data['paper_machine_name'])
                x.insert(2,product_data['product_short_description'])
                x.insert(3,profit_data['profit_code'])
                x.insert(4,product_data['product_description'])
                x.insert(5,product_data['category_product']['category_code'])
                x.insert(0,' ')
                del x[7:11]
                # x.insert(33,' ')
                # x.insert(51,' ')
                worksheet.write_row('A'+str(numb),tuple(x))
                numb+=1

                            

            numb+=3
            worksheet.write('B'+str(numb),'After Sales Master is locked for updating input master for machine production will be opened',merge_format2)
            worksheet.write('B'+str(numb+1),'and data from column B to Column M will get auto populated from sales master on selecting the machine code',merge_format2)
            workbook.close()
            logger.info("succesfully created excel file in required path")
            return send_file(home+'/machine_production_data.xlsx', as_attachment=True)
            # return({"success":True,"data":"data"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})    

