from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Product_Images
from schemas.product_image import Product_ImagesSchema
import os
import boto3

class GetCreateProduct_images(Resource):
    def __init__(self):
        pass

    # call to get all the product images
    def get(self):
        product_image = db.session.query(Product_Images).order_by(Product_Images.id).all()
        if product_image:
            schema = Product_ImagesSchema(many = True)
            data = schema.dump(product_image).data
            return data
        else:
            return("No product images available")

    # call to add the data to product_images
    def post(self):
        file = request.files['image']
        upload_folder = os.path.basename('/product_image')
        f = os.path.join(upload_folder, file.filename)
        file.save(f)
        s3 = boto3.client('s3')
        url = "{}/{}/{}".format(s3.meta.endpoint_url,'prasanth-mall',f)
        s3.upload_file(f,'prasanth-mall',f)
        da = request.form
        dit ={key:value for key,value in da.items()}
        dit['image'] = url
        schema = Product_ImagesSchema()
        new_product_image = schema.load(dit,session=db.session).data
        if new_product_image:
            db.session.add(new_product_image)
            db.session.commit()
            data = schema.dump(new_product_image).data
            return data
        else:
            return ("failed to add the data")
