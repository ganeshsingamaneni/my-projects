from models.file_details import Files_Details
from models.names_model import Outlet_Details
# from schemas.namesschema import Names_Get_Schema
from config import ma, db

# User_output_file_details = ma.Nested(Accounts_Schema)

class Files_Details_Schema(ma.ModelSchema):

    class Meta:
        model = Files_Details
        fields = ('Outlet_name_id','breakfast','lunch','snacks','dinner','total','date','day')#,'date_time')
        sqla_session = db.session


class Files_Details_Get_Schema(ma.ModelSchema):

    class Meta:
        model = Files_Details
        sqla_session = db.session