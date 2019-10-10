from config import db
import datetime
from models.nsr_data_information import Nsr_Data_Information


class Financial_Year_Master(db.Model):
    __tablename__ = "financial_year_master"
    id = db.Column(db.Integer, primary_key=True)
    financial_year_code = db.Column(db.String(50), nullable=False)
    financial_year_name = db.Column(db.String(50), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    # financial_year_nsr_data = db.relationship("Nsr_Data_Information",
    #                               backref=db.backref("nsr_data_financial_year"))