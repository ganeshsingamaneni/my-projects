from datetime import datetime
from flask_restful import Resource
from config import db
from models import Products
from schemas.products import ProductsSchema


class GetActiveProducts(Resource):
    def __init__(self):
        pass

    def get(self):
        # call to get the active products
        products = db.session.query(Products).filter(Products.status == 1).all()
        if products:
            schema = ProductsSchema()
            data = schema.dump(products,many=True).data
            return data
        return("no product with such status")

class GetProductsByProduct_Class(Resource):
    def __init__(self):
        pass
    def get(self,id):
        # call to get the sizes by products
        products = db.session.query(Products).filter(Products.productclass_id == id).all()
        if products:
            schema = ProductsSchema()
            data = schema.dump(products,many=True).data
            return data
        return("no sizes with such product-class")

'''
class GetProductsBy_size(Resource):
    def __init__(self):
        pass
    def get(self,size):
        # call to get the products by name
        products = db.session.query(Products).filter(Products.size.like('%'+size+'%')).all()
        if products:
            schema = ProductsSchema()
            data = schema.dump(products,many=True).data
            return data
        return("no sizes with such size")
'''
