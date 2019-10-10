from models.profit_center_master import Profit_Center_Master
from config import ma, db
from models.pm_master import Paper_Machine_Master
from schemas.pm_master_schema import PMMasterSchema


class Profit_Center_Master_Schema(ma.ModelSchema):

    class Meta:
        model = Profit_Center_Master
        fields = ("profit_code","profit_name","paper_machine_id","updated_at",)
        sqla_session = db.session


class Profit_Center_Master_Get_schema(ma.ModelSchema):
    paper_profit = ma.Nested(PMMasterSchema)
    class Meta:
        model = Profit_Center_Master
        sqla_session = db.session
