from models.time_balancing import Time_Balancing
from config import ma, db
from models.product_master import Product_Master
from models.pm_master import Paper_Machine_Master
from schemas.product_master_schema import ProductMaster_Get_Schema
from schemas.pm_master_schema import PMMasterSchema


class Time_Balancing_Schema(ma.ModelSchema):

    class Meta:
        model = Time_Balancing
        fields = ("work_center_code","profit_center_code","updated_at",)
        sqla_session = db.session


class Time_Balancing_Get_schema(ma.ModelSchema):
    time_balancing_product = ma.Nested(ProductMaster_Get_Schema)
    time_balance_paper_machine = ma.Nested(PMMasterSchema)


    class Meta:
        model = Time_Balancing
        sqla_session = db.session
