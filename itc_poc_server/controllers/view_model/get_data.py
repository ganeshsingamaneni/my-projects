
import string
import xlsxwriter
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/view_data.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_view_data')
loggers = logging.getLogger("view_data_console")


class Get_View_Model_excel(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            request_data = request.get_json()
            workbook = xlsxwriter.Workbook(home+'/View_data.xlsx')
            worksheet = workbook.add_worksheet()
            data_format1 = workbook.add_format({'bg_color': 'yellow'})
            data_format2 = workbook.add_format({'font_color': 'pink'})
            data_format3 = workbook.add_format({'bg_color':'green'})
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': '#FFC7CE'})
            merge_format2 = workbook.add_format({
                'border': 1,
                'valign': 'vcenter',
                'fg_color': '#00C7CE'})
            merge_format3 = workbook.add_format({
                'bold': 1,
                'border': 1})

            worksheet.merge_range(
                'A1:H1', 'BOM FORMAT FOR PAPER MACHINES - PLANNING CYCLE', merge_format)
            worksheet.merge_range('I1:I2', "LY Plan", merge_format)
            worksheet.merge_range('J1:J2', "Actual TD Oct 18", merge_format)
            worksheet.merge_range('K1:K2', "Plan 2019-20", merge_format)
            worksheet.write('L1', '« GSM wise BOM details »', merge_format)
            worksheet.write('M1', 'BOM 01', merge_format)
            worksheet.write('N1', 'BOM 02', merge_format)
            worksheet.write('O1', 'BOM 03', merge_format)

            worksheet.merge_range('A2:D2', 'Unit', merge_format2)
            worksheet.merge_range('E2:F2', request_data['unit'], merge_format3)
            worksheet.write('L2', 'Mix %', merge_format3)
            worksheet.write('M2',request_data['mix']['mix1'] , merge_format3)
            worksheet.write('N2',request_data['mix']['mix2'] , merge_format3)
            worksheet.write('O2',request_data['mix']['mix3'] , merge_format3)

            worksheet.write('I3', request_data['lyplan'], merge_format3)
            worksheet.write('J3', request_data['actualPlan'], merge_format3)
            worksheet.write('L3', 'Reel/Sheet %', merge_format3)
            worksheet.write('M3',request_data['reel']['reel1'] , merge_format3)
            worksheet.write('N3',request_data['reel']['reel2'] , merge_format3)
            worksheet.write('O3',request_data['reel']['reel3'] , merge_format3)
            worksheet.merge_range('A4:D4', 'Machine NO', merge_format2)
            worksheet.merge_range(
                'E4:F4', request_data['machineNbr'], merge_format3)
            worksheet.write('L4', 'GSM %', merge_format3)
            worksheet.write('M3',request_data['gsm']['gsm1'] , merge_format3)
            worksheet.write('N4',request_data['gsm']['gsm2'] , merge_format3)
            worksheet.write('O4',request_data['gsm']['gsm3'] , merge_format3)
            worksheet.merge_range('A6:D6', 'Distribution Channel', merge_format2)
            worksheet.merge_range(
                'E6:F6', request_data['distributionChannel'], merge_format3)
            worksheet.merge_range('A8:D8', 'Description', merge_format2)
            worksheet.merge_range(
                'E8:F8', request_data['description'], merge_format3)

            worksheet.write('A11', 'Material', merge_format)
            worksheet.write('B11', 'Imp Ind', merge_format)
            worksheet.write('C11', ' ', merge_format)
            worksheet.write('D11', 'Cat', merge_format)
            worksheet.merge_range('E11:F11', "Material Description", merge_format)
            worksheet.write('G11', 'Bun', merge_format)
            worksheet.write('H11', 'Ret%', merge_format)
            worksheet.write('I11', '2018-19', merge_format)
            worksheet.write('J11', 'TD Oct 18', merge_format)
            worksheet.write('K11', 'Plan 2018-19', merge_format)
            worksheet.write('L11', 'Mix is 100% :ok', merge_format)
            worksheet.write('M11', 'BOM 01', merge_format)
            worksheet.write('N11', 'BOM 02', merge_format)
            worksheet.write('O11', 'BOM 03', merge_format)

            data_to_assiagn = request_data['bomData']
            pulp = []
            Coating_Chemicals = []
            Oxidised_Starch = []
            Wetend_Starch = []
            Filler = []
            Strach_Filter_subtotal = []
            Pulp_Coating_Subtotal = []
            Other_Chemicals = []
            Machine_info=[]
            grand_total = data_to_assiagn[-1]
            for x in data_to_assiagn:
                keys = list(x.keys())
                if 'catType' in keys:
                    if (x['catType'] == 'pulp') or (x['catType'] == 'pulp_sub_total') :
                        pulp.append(list(x.values()))
                    elif (x['catType'] == 'coating_chemicals') or (x['catType'] == 'coating_chemicals_sub_total'):
                        Coating_Chemicals.append(list(x.values()))
                    elif x['catType'] == "starch_and_filter_sub_total":
                        Strach_Filter_subtotal.append(list(x.values()))
                    elif x['catType'] == "pulp_coating_starch_sub_total":
                        Pulp_Coating_Subtotal.append(list(x.values())) 
                    elif (x['catType'] == "other_chemicals") or (x['catType']== "other_chemicals_sub_total"):
                        Other_Chemicals.append(list(x.values())) 
                    elif x['catType'] == "machine_info":
                        Machine_info.append(list(x.values()))
                if 'subCatType' in keys: 
                    if x["subCatType"] == "oxidised_starch":
                        Oxidised_Starch.append(list(x.values()))
                    elif x["subCatType"] == "wetend_starch":
                        Wetend_Starch.append(list(x.values()))
                    elif x["subCatType"] == "filler":
                        Filler.append(list(x.values())) 
                    else:
                        pass    
                else:
                    pass        


                        
            empty_row = []
            for x in range(14):
                empty_row.append(" ")
            sub_pulp = pulp[-1]
            var = sub_pulp[4]
            del sub_pulp[4]
            del sub_pulp[-1]
            del pulp[-1]
            empty_row.insert(4, 'Pulp')
            worksheet.write_row('A12', tuple(empty_row), cell_format=data_format2)
            n = 13
            for x in pulp:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            sub_pulp.insert(0,' ')
            sub_pulp.insert(1,' ')
            sub_pulp.insert(2,' ')
            sub_pulp.insert(3,' ')
            sub_pulp.insert(6,var)
            sub_pulp.insert(5,' ')
            worksheet.write_row('A'+str(n), tuple(sub_pulp),
                                cell_format=data_format1)
            n += 1
            empty_row[4] = 'Coating Chemicals'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)
            
            n += 1
            sub_coating = Coating_Chemicals[-1]
            var1 = sub_coating[4]
            del sub_coating[4]
            del sub_coating[-1]
            sub_coating.insert(0,' ')
            sub_coating.insert(1,' ')
            sub_coating.insert(2,' ')
            sub_coating.insert(3,' ')
            sub_coating.insert(6,var1)
            sub_coating.insert(5,' ')
            del Coating_Chemicals[-1]

            for x in Coating_Chemicals:
                x.insert(2,'  ')
                x.insert(5,' ')
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                del x[-1]
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            worksheet.write_row('A'+str(n), tuple(sub_coating),
                                cell_format=data_format1)

            n += 1
            empty_row[4] = 'Starch & Filler Chemicals'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)
            n += 1
            empty_row[4] = 'Oxidised Starch'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)


            n += 1
            for x in Oxidised_Starch:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                desc1 = x[3]
                x[3] = 'OS'
                x.insert(6,desc1)
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1

            empty_row[4] = 'Wetend Starch'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)

            n += 1
            for x in Wetend_Starch:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                x.insert(6,'KG')
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            empty_row[4] = 'Filler'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)
            n += 1
            for x in Filler:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                x.insert(6,'KG')
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            strach_fil_sub = Strach_Filter_subtotal[0]  
            strach_fil_sub.insert(0," ")
            strach_fil_sub.insert(1," ") 
            strach_fil_sub.insert(2," ") 
            strach_fil_sub.insert(3," ")
            strach_fil_sub.insert(5," ")
            strach_fil_sub.insert(6," ")
            strach_fil_sub.insert(7," ")
            del strach_fil_sub[-1]
            worksheet.write_row('A'+str(n), tuple(strach_fil_sub),
                                cell_format=data_format1)
            n += 1
            empty_row[4] = '    '
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)

            pulp_coat_sub = Pulp_Coating_Subtotal[0]
            pulp_coat_sub.insert(0," ")
            pulp_coat_sub.insert(1," ") 
            pulp_coat_sub.insert(2," ") 
            pulp_coat_sub.insert(3," ")
            pulp_coat_sub.insert(5," ")
            pulp_coat_sub.insert(6," ")
            pulp_coat_sub.insert(7," ") 
            del pulp_coat_sub[-1]                   
            n += 1
            worksheet.write_row('A'+str(n), tuple(pulp_coat_sub),
                                cell_format=data_format1)
            n += 1

            empty_row[4] = 'Other Wet End Chemicals'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format2)
            n += 1
            del Other_Chemicals[-1]
            for x in Other_Chemicals:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                x.insert(6,"KG")
                x.insert(7,"  ")
                
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            empty_row[4] = 'Other Chemicals'
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format1)
            n += 1
            
            for x in Machine_info:
                x.insert(2,'  ')
                x.insert(5,' ')
                del x[-1]
                desc = x[0]
                del x[0]
                x.insert(4,desc)
                x.insert(6,'Oth')
                x.insert(7,"  ")
                worksheet.write_row('A'+str(n), tuple(x))
                n += 1
            empty_row[4] = '    '
            worksheet.write_row('A'+str(n), tuple(empty_row),
                                cell_format=data_format1)
            
            grand_total_values = list(grand_total.values())
            grand_total_values.insert(0," ")
            grand_total_values.insert(1," ") 
            grand_total_values.insert(2," ") 
            grand_total_values.insert(3," ")
            grand_total_values.insert(5," ")
            grand_total_values.insert(6," ")
            grand_total_values.insert(7," ")
            del grand_total_values[-1]
            grand_total_values.insert(10," ")
            grand_total_values.insert(11," ")
            n += 1
            worksheet.write_row('A'+str(n), tuple(grand_total_values),
                                cell_format=data_format3)
            workbook.close()
            logger.info("succesfully created excel file in required path")
            return send_file(home+'/View_data.xlsx', as_attachment=True)
            #return({"success": True, "data": "data"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message":str(e)})
