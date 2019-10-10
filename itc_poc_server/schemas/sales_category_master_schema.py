from models.sales_category_master import Sales_Category_Master
from config import ma, db


class Sales_Category_Master_Schema(ma.ModelSchema):

    class Meta:
        model = Sales_Category_Master
        fields = ("sales_category_code","sales_category_description","updated_at",)
        sqla_session = db.session


class Sales_Category_Master_Get_schema(ma.ModelSchema):

    class Meta:
        model = Sales_Category_Master
        sqla_session = db.session
