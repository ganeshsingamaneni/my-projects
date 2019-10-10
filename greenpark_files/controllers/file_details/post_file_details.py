import datetime
from datetime import datetime
from datetime import date, timedelta
from sqlalchemy import and_, func, extract
import os
import calendar
import xlsxwriter
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
from schemas.filedetailsschema import Files_Details_Schema, Files_Details_Get_Schema
from flask import make_response, request, send_file
from os.path import expanduser
home = expanduser("~")

# CONFIG_PATH = os.path.join(basedir, 'loggeryaml/file_details.yaml')
# logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
# logger = logging.getLogger('postfile_data')
# loggers = logging.getLogger("file_dataconsole")
today = datetime.today()
datem = datetime(today.year, today.month, 1)
# today = date.today()
# today_date = today.strftime("%d-%m-%Y")


class File_Details(Resource):
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

    def post(self):
        try:
            file1 = request.files['file1']
            upload_folder = os.path.basename('/upload')
            f = os.path.join(upload_folder, file1.filename)
            file1.save(f)
            data_df = main_func(f)
            out_name = db.session.query(Outlet_Details).order_by(
                Outlet_Details.Outlet_id).all()
            if out_name:
                schema = Names_Schema(many=True)
                data = schema.dump(out_name)
                names_ids = []
                for d in data:
                    gaga = d['Outlet_id']
                    if gaga not in names_ids:
                        names_ids.append(gaga)
            names_list = {}
            for x in data:
                names_list.update({x['Outlet_Name']: x['Outlet_id']})
            yesterday_ = today - timedelta(days=1)
            yest_ = str(yesterday_)
            yes = str(yesterday_)
            yes1 = yes[8:10]+'-'+yes[5:7]+'-'+yes[:4]
            born = datetime.strptime(yes1, '%d-%m-%Y').weekday()
            day = calendar.day_name[born]
            # for x in data_df:
            #     schema = Files_Details_Schema()
            #     d_to_l = list(x.keys())
            #     iid = names_list[d_to_l[0]]
            #     add_dict={'Outlet_name_id': iid, 'breakfast': x['BREAK FAST'], 'lunch': x['LUNCH'],
            #         'snacks': x['SNACKS'], 'dinner': x['DINNER'], 'total': x['Total'],'date':yest_[:10],'day':day}#,'date_time':yesterday}
            #     new_hotel = schema.load(add_dict, session=db.session)
            #     db.session.add(new_hotel)
            #     db.session.commit()
            get_data = db.session.query(Files_Details).filter(
                extract('month', Files_Details.created_at) == datetime.today().month).all()
            if get_data:
                schema = Files_Details_Get_Schema(many=True)
                data_ = schema.dump(get_data)
                da_frame = pd.DataFrame(data_)
                new_df = da_frame[['files_name', 'breakfast',
                                   'lunch', 'snacks', 'dinner', 'total', 'date', 'day']]
                json_lists = []
                for region, df_region in new_df.groupby('date'):
                    df_list = df_region.to_dict('records')
                    json_lists.append(df_list)
                dfObj = pd.DataFrame(columns=['Type', 'Quantity'])
                outlet_types = db.session.query(Outlet_Details).all()
                if outlet_types:
                    schema = Names_Schema(many=True)
                    data_outlet_names = schema.dump(outlet_types)
                    naya_ids = []
                    for xuv in data_outlet_names:
                        gaga = xuv['Outlet_id']
                        if gaga not in naya_ids:
                            naya_ids.append(gaga)

                for no in json_lists:
                    emp = []
                    for cc in no:
                        emp.append(cc['files_name'])
                    for idid in naya_ids:
                        if idid in emp:
                            pass
                        else:
                            a = {'files_name': idid, 'breakfast': 0, 'lunch': 0,
                                 'snacks': 0, 'dinner': 0, 'total': 0, 'date': 'none', 'day': 'None'}
                            no.append(a)
                for x in json_lists:
                    if json_lists.index(x) is 0:
                        bcbc = sorted(x, key=lambda i: i['files_name'])
                        for yuu in bcbc:
                            res = dict((v, k) for k, v in names_list.items())
                            res.update({0: "Empty"})
                            type_id = yuu['files_name']
                            yuu[res[type_id]] = yuu.pop('files_name')
                            df = pd.DataFrame(yuu, index=[0, 1, 2, 3, 4, 5, 6])
                            dfs = df.transpose()
                            vv = dfs.reset_index()
                            vv.columns = ['Type', 'Quantity', 'Quantity1',
                                          "Quantity2", "Quantity3", "Quantity4", "quantity5", "quantity6"]
                            nn = vv[['Type', 'Quantity']]
                            list1 = nn.to_dict('records')
                            list2 = list1[-1:] + list1[:-1]
                            if bcbc.index(yuu) is 0:
                                list3 = list2[-2:] + list2[:-2]
                                list3[2]['Quantity'] = ' '
                                dfObj = dfObj.append(list3, ignore_index=True)
                            else:
                                list2.pop()
                                list2.pop()
                                list2[0]['Quantity'] = ' '
                                dfObj = dfObj.append(list2, ignore_index=True)
                    else:
                        ind = json_lists.index(x)
                        ll = []
                        bcbc = sorted(x, key=lambda i: i['files_name'])
                        for y in bcbc:
                            res = dict((v, k) for k, v in names_list.items())
                            res.update({0: "Empty"})
                            type_id = y['files_name']
                            y[res[type_id]] = y.pop('files_name')
                            values = y.values()
                            if bcbc.index(y) is 0:
                                la_val = list(values)
                                ll2 = la_val[-1:] + la_val[:-1]
                                ll3 = ll2[-2:] + ll2[:-2]
                                ll3[2] = ' '
                                ll.extend(ll3)
                            else:
                                lala = list(values)
                                ll2 = lala[-1:] + lala[:-1]
                                ll2[0] = ' '
                                ll.extend(ll2[:-2])
                        dfObj.insert(ind+1, "quantity"+str(ind), ll)

            gdg = dfObj.rename(columns=dfObj.iloc[0]).drop(dfObj.index[0])
            to_dict = gdg.to_dict()
            grand_total = ['grand total']
            for x, y in to_dict.items():
                if x != 'date':
                    grand_total.append(
                        y[7]+y[13]+y[19]+y[25]+y[31]+y[37]+y[43])
            columns_list = list(gdg.columns)
            df = gdg.append(pd.DataFrame(
                [grand_total], index=['e'], columns=columns_list))
            df_to_lists = df.values.tolist()
            columns_list[0] = ' '
            df_to_lists.insert(0, columns_list)
            llength = len(columns_list)-1
            month_append = [' '] * llength
            month_append.insert(0, "Report for the month")
            df_to_lists.insert(0, month_append)
            df_to_lists[2][0] = ' '
            hsh = []
            for dd in df_to_lists:
                if 0 in dd:
                    a = [" " if x == 0 else x for x in dd]
                    hsh.append(a)
                else:
                    hsh.append(dd)    
            # print(hsh)
            # print(df_to_lists)
            workbook = xlsxwriter.Workbook('/home/ganesh/Desktop/demo.xlsx')
            worksheet = workbook.add_worksheet()
            l2l2 =[]
            for i in range(3,len(hsh),6):
                l2l2.append(i)
            for x in hsh:
                # print(x,"////")
                cc = hsh.index(x)
                c = cc+1   
                cell_fo = workbook.add_format({'bold': True})
                cell_fo2 = workbook.add_format({'font_color': 'red'})

                if cc in [0,1,2]:
                    worksheet.write_row('A'+str(c),tuple(x),cell_fo)
                elif cc in l2l2:
                    worksheet.write_row('A'+str(c),tuple(x),cell_fo2) 
                else:
                    worksheet.write_row('A'+str(c),tuple(x)) 
            workbook.close()

            # df.to_excel("/home/ganesh/Desktop/CoverAnalysisFromIDS.xlsx",
            #         index=False, columns=columns_list)
            return ({"success": True, "message": "data"})
        except Exception as e:
            # logger.exception("get data of output file details is Failed")
            return ({"success": False, "message": str(e)})
