from models.financial_year_master import Financial_Year_Master
from config import ma, db


class Financial_Year_Master_schema(ma.ModelSchema):

    class Meta:
        model = Financial_Year_Master
        fields = ("financial_year_code","financial_year_name","updated_at")
        sqla_session = db.session


class Financial_Year_Master_Get_schema(ma.ModelSchema):

    class Meta:
        model = Financial_Year_Master
        sqla_session = db.session
