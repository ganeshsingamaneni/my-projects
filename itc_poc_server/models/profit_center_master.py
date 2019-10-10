from config import db
import datetime
from models.product_master import Product_Master
from models.nsr_data_information import Nsr_Data_Information


class Profit_Center_Master(db.Model):
    __tablename__ = "profit_center_master"
    id = db.Column(db.Integer, primary_key=True)
    profit_code = db.Column(db.String(50), nullable=False)
    profit_name = db.Column(db.String(50), nullable=False)
    paper_machine_id = db.Column(db.Integer,
                                 db.ForeignKey('paper_machine_master.id'),
                                 nullable=False)
                                 
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)
    product = db.relationship("Product_Master",
                              backref=db.backref("profit_product"))

    # profit_center_nsr_data =  db.relationship("Nsr_Data_Information",
    #                           backref=db.backref("nsr_data_profit_center"))                         