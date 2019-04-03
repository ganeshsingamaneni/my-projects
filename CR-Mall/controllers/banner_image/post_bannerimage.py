from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request, render_template
from models import Banner_images
from schemas.banner_image import BannerImageSchema, BannerImageGetSchema
import os
import boto3
import json
from datetime import date, datetime
from sqlalchemy import and_



class GetCreateBanner_images(Resource):
    def __init__(self):
        pass

    # call to get all the banner images
    def get(self):
        banner = db.session.query(Banner_images).order_by(Banner_images.id).all()
        if banner:
            schema = BannerImageGetSchema(many = True)
            data = schema.dump(banner).data
            return data
        else:
            return("No banner images available")

    # call to add the data to product_images
    def post(self):
        file = request.files['image']
        upload_folder = os.path.basename('/banner_image')
        f = os.path.join(upload_folder, file.filename)
        file.save(f)
        s3 = boto3.client('s3')
        url = "{}/{}/{}".format(s3.meta.endpoint_url,'prasanth-mall',f)
        s3.upload_file(f,'prasanth-mall',f)
        da = request.form
        dit ={key:value for key,value in da.items()}
        dit['image'] = url
        existing_image = db.session.query(Banner_images).filter(Banner_images.image == url).first()
        if existing_image is None:
            schema = BannerImageSchema()
            new_banner_image = schema.load(dit,session=db.session).data
            db.session.add(new_banner_image)
            db.session.commit()
            data = schema.dump(new_banner_image).data
            return data
        else:
            return ("banner image data already exists")

class GetBanner_imagespages(Resource):
    def __init__(self):
        pass

    def get(self,start,end):
       banner = db.session.query(Banner_images).filter(and_(Banner_images.id>=start,Banner_images.id<=end)).all()
       if banner:
           schema = BannerImageSchema()
           data = schema.dump(banner,many=True).data
           return data
       return("not found")

    '''
    # call to get all the banner images
    def get(self,page):
        banner = db.session.query(Banner_images).order_by(Banner_images.id).all()
        if banner:
            banner_image = Banner_images.query.paginate(page,6,error_out=True)
            schema = BannerImageSchema(many = True)
            obj = banner_image.items
            data = schema.dump(obj).data
            all_pages = banner_image.iter_pages()
            for i in all_pages:
                print(i)
            return data

        else:
            return("No banner images available")
    '''
