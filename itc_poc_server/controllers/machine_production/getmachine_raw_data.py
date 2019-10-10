from flask_restful import Resource, request
from schemas.machine_raw_data_schema import machine_raw_data_schema,Product_master_schema,Nsr_info_schema
from models.product_master import Product_Master
from models.nsr_data_information import Nsr_Data_Information
from schemas.nsr_data_information_schema import Nsr_Data_2_Schema
from schemas.product_master_schema import ProductMaster_Get_Schema
from models.machine_production_data_information import Machine_Production_Data_Information
from schemas.machine_production_data_information_schema import Machine_Production_Data_Information_Get_schema
from config import ma, db



class Get_machine_raw_data(Resource):
    def __init__(self):
        pass


    def get(self, id):
        '''
        raw data for machine production sheet
        '''
        try:
            get_pm = db.session.query(Nsr_Data_Information).order_by(
                Nsr_Data_Information.paper_machine_id == id
            )
            if get_pm:
                schema=Nsr_info_schema(many=True)
                data = schema.dump(get_pm)
                finalData = []
                for each in data:
                    product = db.session.query(Product_Master).filter(Product_Master.id == int(each["product_id"])).first()
                    if product:
                        product_schema = ProductMaster_Get_Schema()
                        product_schema_data  = product_schema.dump(product)
                        machineprodcutiondata = db.session.query(Machine_Production_Data_Information).filter(Machine_Production_Data_Information.product_id == each["product_id"]).first()
                        if machineprodcutiondata:
                            machine_production_schema = Machine_Production_Data_Information_Get_schema()
                            machine_production_schema_data = machine_production_schema.dump(machineprodcutiondata)
                            each["machineproduction"] = machine_production_schema_data
                        each["product"]=product_schema_data                    
                return {"success": True, "data": data}

            else:
                # logger.info("No data is found on this id")
                return {
                    "success": False,
                    "message": "No data is found on this id"
                }

        except Exception as e:
            return ({"success":False,"message":str(e),"data":None})
