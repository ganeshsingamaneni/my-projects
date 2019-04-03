from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Banner_images
from schemas.banner_image import BannerImageSchema, BannerImageGetSchema
import os




class GetActiveBannerImages(Resource):
    def __init__(self):
        pass

    # call to get the active banner images
    def get(self):
        banner_image = db.session.query(Banner_images).filter(Banner_images.status == True).all()
        if banner_image:
            schema = BannerImageGetSchema()
            data = schema.dump(banner_image,many=True).data
            return data
        else:
            return("no banner image with such status")
