from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Categories
from schemas.categories import CategoriesSchema, CategoryGetSchema
from exceptions import PostFailed
import os

class GetActiveCategories(Resource):
    def __init__(self):
        pass

    # call to get the active categories
    def get(self):
        categories = db.session.query(Categories).filter(Categories.status == True).all()
        if categories:
            schema = CategoryGetSchema()
            data = schema.dump(categories,many=True).data
            return data
        else:
            return("no category with such status")


class GetCategorieBy_name(Resource):
    def __init__(self):
        pass

    # call to get the categorie by name
    def get(self,name):
        categories = db.session.query(Categories).filter(Categories.name == name).all()
        if categories:
            schema = CategoryGetSchema()
            data = schema.dump(categories,many=True).data
            return data
        else:
            return("no category with such name")
