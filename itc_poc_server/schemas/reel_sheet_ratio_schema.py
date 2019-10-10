from models.reel_sheet_ratio import Reel_Sheet_Ratio
from config import ma, db
from models.pm_master import Paper_Machine_Master
from models.product_master import Product_Master
from schemas.pm_master_schema import PMMasterSchema
from schemas.product_master_schema import ProductMaster_Get_Schema

class Reel_Sheet_Ratio_Schema(ma.ModelSchema):

    class Meta:
        model = Reel_Sheet_Ratio
        fields = ("paper_machine_id","product_code_id","updatedAt")
        sqla_session = db.session


class Reel_Sheet_Ratio_Get_schema(ma.ModelSchema):
    reel_sheet_ratio_paper_machine = ma.Nested(PMMasterSchema)
    reel_sheet_ratio_product = ma.Nested(ProductMaster_Get_Schema)      

    class Meta:
        model = Reel_Sheet_Ratio
        sqla_session = db.session
