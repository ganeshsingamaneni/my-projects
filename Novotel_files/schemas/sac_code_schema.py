from models.sac_code_model import Sac_Tran_Codes_Mapping
from config import ma,db

class Sac_code_Schema(ma.ModelSchema):
    class Meta:
        model = Sac_Tran_Codes_Mapping
        sqla_session = db.session