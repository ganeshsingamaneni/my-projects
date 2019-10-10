from config import ma, db
from models.pm_master import Paper_Machine_Master
from models.profit_center_master import Profit_Center_Master
from models.product_master import Product_Master
from models.category_master import Category_Master
from models.nsr_data_information import Nsr_Data_Information



class machine_raw_data_schema(ma.ModelSchema):
    class Meta:
        model = Paper_Machine_Master
        sqla_session = db.session

class profit_center_master_schema(ma.ModelSchema):
    paper_profit = ma.Nested(machine_raw_data_schema)
    class Meta:
        model = Profit_Center_Master
        sqla_session = db.session

class category_master_schema(ma.ModelSchema):
    class Meta:
        model = Category_Master
        sqla_session = db.session


class Product_master_schema(ma.ModelSchema):
    class Meta:
        model = Product_Master
        sqla_session = db.session


class Nsr_info_schema(ma.ModelSchema):
    #nsr_data_paper_machine = ma.Nested(machine_raw_data_schema)
    #profit_product = ma.Nested(profit_center_master_schema)
    #category_product = ma.Nested(category_master_schema)
    class Meta:
        model = Nsr_Data_Information
        sqla_session = db.session





