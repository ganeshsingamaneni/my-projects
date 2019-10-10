from config import db
import datetime
from models.reel_sheet_ratio import Reel_Sheet_Ratio
from models.time_balancing import Time_Balancing
from models.nsr_data_information import Nsr_Data_Information

class Product_Master(db.Model):
    __tablename__ = "product_master"
    id = db.Column(db.Integer, primary_key=True)
    product_short_description = db.Column(db.Text, nullable=False)
    profit_center_id = db.Column(db.Integer,
                                 db.ForeignKey('profit_center_master.id'),
                                 nullable=False)
    product_category_id = db.Column(db.Integer(),
                                    db.ForeignKey('category_master.id'),
                                    nullable=False)
    mill_reel = db.Column(db.Text, nullable=True)
    mill_sheet = db.Column(db.Text, nullable=True)
    convertors_sheet = db.Column(db.Text, nullable=True)
    core_wrapper = db.Column(db.String(200),nullable = True)

    product_description = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    product_reel_sheet_ratio = db.relationship("Reel_Sheet_Ratio",
                                  backref=db.backref("reel_sheet_ratio_product"))
    product_time_balancing = db.relationship("Time_Balancing",
                                  backref=db.backref("time_balancing_product"))                              

    # product_nsr_data = db.relationship("Nsr_Data_Information",
                                #   backref=db.backref("nsr_data_product")) 