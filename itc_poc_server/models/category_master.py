from config import db
import datetime
from models.product_master import Product_Master
from models.input_master import Input_Master


class Category_Master(db.Model):
    __tablename__ = "category_master"
    id = db.Column(db.Integer, primary_key=True)
    category_code = db.Column(db.String(50), nullable=False)
    category_name = db.Column(db.String(50), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)
    product = db.relationship("Product_Master",
                              backref=db.backref("category_product"))
    master_input = db.relationship("Input_Master",
                              backref=db.backref("category_input"))
