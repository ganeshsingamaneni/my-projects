from config import db
import datetime
from models.nsr_data_information import Nsr_Data_Information



class Segment_Master(db.Model):
    __tablename__ = "segment_master"
    id = db.Column(db.Integer, primary_key=True)
    segment_code = db.Column(db.String(50), nullable=False)
    segment_name = db.Column(db.String(50), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    # segment_nsr_data = db.relationship("Nsr_Data_Information",
    #                               backref=db.backref("nsr_data_segment"))