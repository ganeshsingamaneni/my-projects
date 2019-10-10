from config import db
import datetime
from models.input_master import Input_Master


class UOM_Master(db.Model):
    __tablename__ = "uom_master"
    id = db.Column(db.Integer, primary_key=True)
    uom_code = db.Column(db.String(50), nullable=False)
    uom_name = db.Column(db.String(50), nullable=False)
    uom_conversion_factor = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)
    inputmaster = db.relationship("Input_Master",
                              backref=db.backref("input_uom"))