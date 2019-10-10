from config import ma, db
from models.pm_master import Paper_Machine_Master


class PMMasterSchema(ma.ModelSchema):
    class Meta:
        model = Paper_Machine_Master
        sqla_session = db.session

