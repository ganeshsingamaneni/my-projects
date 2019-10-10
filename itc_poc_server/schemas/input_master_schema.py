from models.input_master import Input_Master
from models.category_master import Category_Master
from models.uom_master import UOM_Master
from models.gl_master import GL_Master
from schemas.uom_schema import Uom_Master_Get_schema
from schemas.category_master_schema import Category_Master_Get_schema
from schemas.gl_master_schema import GLMasterSchema
from config import ma, db


class Input_Master_schema(ma.ModelSchema):

    class Meta:
        model = Input_Master
        fields = ("category_code_id","sap_code","sap_description","material_type","uom_id","rate","gl_id")
        sqla_session = db.session


class Input_Master_Get_schema(ma.ModelSchema):
    input_uom = ma.Nested(Uom_Master_Get_schema)
    category_input = ma.Nested(Category_Master_Get_schema)
    input_gl = ma.Nested(GLMasterSchema)    

    class Meta:
        model = Input_Master
        sqla_session = db.session
