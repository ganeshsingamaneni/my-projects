from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Product_Images
from schemas.product_image import Product_ImagesSchema
import os


class GetActiveProductImages(Resource):
    def __init__(self):
        pass

    def get(self):
        # call to get the active product_class
        product_images = db.session.query(Product_Images).filter(Product_Images.status == True).all()
        if product_images:
            schema = Product_ImagesSchema()
            data = schema.dump(product_images,many=True).data
            return data
        else:
            return("no product image with such status")

class GetProductImageByProduct(Resource):
    def __init__(self):
        pass

    def get(self,id):
        # call to get the product_image by product
        product = db.session.query(Product_Images).filter(Product_Images.product_id == id).all()
        if product:
            schema = Product_ImagesSchema()
            data = schema.dump(product,many=True).data
            return data
        else:
            return("no product images  with such product")
