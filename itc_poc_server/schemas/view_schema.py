from models.view_model import View_Model
from config import ma, db


class View_Model_Schema(ma.ModelSchema):

    class Meta:
        model = View_Model
        sqla_session = db.session



