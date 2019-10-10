from config import ma, db
from models.product_master import Product_Master
from models.profit_center_master import Profit_Center_Master
from models.category_master import Category_Master
from schemas.category_master_schema import Category_Master_Get_schema
from schemas.profit_center_master_schema import Profit_Center_Master_Get_schema


class ProductMasterSchema(ma.ModelSchema):
    class Meta:
        model = Product_Master
        fields = (
            "product_short_description",
            "profit_center_id",
            "product_category_id",
            "product_description",
            "mill_reel",
            "mill_sheet",
            "convertors_sheet",
            "core_wrapper"
        )
        sqla_session = db.session


class ProductMaster_Get_Schema(ma.ModelSchema):
    profit_product = ma.Nested(Profit_Center_Master_Get_schema)
    category_product = ma.Nested(Category_Master_Get_schema)
    class Meta:
        model = Product_Master
        sqla_session = db.session
