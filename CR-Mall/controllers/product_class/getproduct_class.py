from datetime import datetime
from flask_restful import Resource
from config import db
from models import Product_Class
from schemas.product_class import Product_ClassSchema,Product_ClassGetSchema


class GetActiveProductClass(Resource):
    def __init__(self):
        pass

    # call to get the active product-class
    def get(self):
        product_class = db.session.query(Product_Class).filter(Product_Class.status == True).all()
        if product_class:
            schema = Product_ClassSchema()
            data = schema.dump(product_class,many=True).data
            return data
        return("no product_class with such status")

class GetProductClassBy_name(Resource):
    def __init__(self):
        pass

    # call to get the product-class by name
    def get(self,name):
        product_class = db.session.query(Product_Class).filter(Product_Class.name.like('%'+name+'%')).all()
        if product_class:
            schema = Product_ClassSchema()
            data = schema.dump(product_class,many=True).data
            return data
        return("no subcategorie with such name")

class GetProductClassBySubCategory(Resource):
    def __init__(self):
        pass

    # call to get the product-class by category
    def get(self,id):
        product_class = db.session.query(Product_Class).filter(Product_Class.subcategory_id == id).all()
        if product_class:
            schema = Product_ClassSchema()
            data = schema.dump(product_class,many=True).data
            return data
        return("no product_class with such SubCategory")
