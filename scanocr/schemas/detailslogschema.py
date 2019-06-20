from models.scandetaillog import Detailslog
from config import ma,db


class DetailslogSchema(ma.ModelSchema):
    class Meta:
        model = Detailslog
        fields =("person_id","created_by","updated_by","created_at","id","updated_at")
        sqla_session = db.session

class GetDetailslogSchema(ma.ModelSchema):
       class Meta:
           model = Detailslog
           sqla_session = db.session
