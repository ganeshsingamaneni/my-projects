from config import db
import datetime
from models.nsr_data_information import Nsr_Data_Information


class Sales_Category_Master(db.Model):
    __tablename__ = "sales_category_master"
    id = db.Column(db.Integer, primary_key=True)
    sales_category_code = db.Column(db.String(50), nullable=False)
    sales_category_description = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    # sales_category_nsr_data = db.relationship("Nsr_Data_Information",
    #                               backref=db.backref("sales_category_nsr_data"))