from models.file_details import Files_Details
from models.names_model import Outlet_Details
from schemas.filedetailsschema import Files_Details_Schema
from config import ma, db

# User_output_file_details = ma.Nested(Accounts_Schema)

class Names_Schema(ma.ModelSchema):

    class Meta:
        model = Outlet_Details
        sqla_session = db.session


class Names_Get_Schema(ma.ModelSchema):
    files_name = ma.Nested(Files_Details_Schema)

    class Meta:
        model = Outlet_Details
        sqla_session = db.session