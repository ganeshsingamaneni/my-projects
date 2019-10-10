from models.segment_master import Segment_Master
from config import ma, db


class Segment_Master_Schema(ma.ModelSchema):

    class Meta:
        model = Segment_Master
        fields = ("segment_code","segment_name","updated_at")
        sqla_session = db.session


class Segment_Master_Get_schema(ma.ModelSchema):

    class Meta:
        model = Segment_Master
        sqla_session = db.session
