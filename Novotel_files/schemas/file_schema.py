from models.file_model import Output_files_Details
from config import ma,db

class Output_Files_Schema(ma.ModelSchema):
    class Meta:
        model = Output_files_Details
        sqla_session = db.session