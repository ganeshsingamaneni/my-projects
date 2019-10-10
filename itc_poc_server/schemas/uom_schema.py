from models.uom_master import UOM_Master
from config import ma, db


class Uom_Master_Schema(ma.ModelSchema):

    class Meta:
        model = UOM_Master
        fields = ("uom_code","uom_name","uom_conversion_factor","updated_at",)
        sqla_session = db.session


class Uom_Master_Get_schema(ma.ModelSchema):

    class Meta:
        model = UOM_Master
        sqla_session = db.session
