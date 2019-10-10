from flask_restful import Api, Resource
from config import ma, db
from models.nsr_data_information import Nsr_Data_Information
from schemas.nsr_data_information_schema import nsr_data_for_time_balancing
from schemas.product_master_schema import ProductMaster_Get_Schema
from models.product_master import Product_Master
from models.machine_production_data_information import Machine_Production_Data_Information
from schemas.machine_production_data_information_schema import Machine_Production_Data_Information_Get_schema



class GetTimeBalancing(Resource):
    def __init__(self):
        pass

    def get(self,id):
        '''get time balancing data'''
        try:
            salesmaster = db.session.query(Nsr_Data_Information).order_by(Nsr_Data_Information.paper_machine_id == str(id))
            if salesmaster:
                salesmaster_schema = nsr_data_for_time_balancing(many=True)
                salesmaster_data = salesmaster_schema.dump(salesmaster)
            for each in salesmaster_data:
                product = db.session.query(Product_Master).filter(Product_Master.id == int(each["product_id"])).first()
                if product:
                    product_schema = ProductMaster_Get_Schema()
                    product_schema_data  = product_schema.dump(product)
                    each["product"]=product_schema_data 
                    machineprodcutiondata = db.session.query(Machine_Production_Data_Information).filter(Machine_Production_Data_Information.product_id == each["product_id"]).first()
                    if machineprodcutiondata:
                        machine_production_schema = Machine_Production_Data_Information_Get_schema()
                        machine_production_schema_data = machine_production_schema.dump(machineprodcutiondata)
                        each["machineproduction"] = machine_production_schema_data
                        
            return ({"success":True,"data":salesmaster_data})
            pass
        except Exception as e:
            return({"success":False,"message":str(e)})


