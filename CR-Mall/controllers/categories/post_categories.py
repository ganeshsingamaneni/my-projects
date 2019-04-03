from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Categories
from schemas.categories import CategoriesSchema, CategoryGetSchema
from exceptions import PostFailed
import os



class GetcreateCategories(Resource):
    def __init__(self):
        pass

    # call to get all the categories
    def get(self):
        category = db.session.query(Categories).order_by(Categories.id).all()
        if category:
            schema = CategoryGetSchema(many = True)
            data = schema.dump(category).data
            return data
        else:
            return("no data is available in categories")

    #call to post the categorie details
    def post(self):

        da = request.get_json()
        name = da['name']
        dit = {key:value for key,value in da.items()}
        #dit['image'] = f
        existing_one = db.session.query(Categories).filter(Categories.name == name).one_or_none()
        if existing_one is None:
            schema = CategoriesSchema()
            new_categorie = schema.load(dit, session=db.session).data
            db.session.add(new_categorie)
            db.session.commit()
            data = schema.dump(new_categorie).data
            return data
        else:
            return ("categorie with this name already exists")
