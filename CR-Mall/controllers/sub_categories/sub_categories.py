from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Sub_Categories
from schemas.sub_categories import Sub_CategoriesSchema, GetSub_CategoriesSchema
from exceptions import PostFailed
import os


class GetUpdateDeleteSub_Categories(Resource):
    def __init__(self):
        pass

    # call to get the categorie based on id
    def get(self,id):
        try:
            categorie = db.session.query(Sub_Categories).filter(Sub_Categories.id == id).first()
            if categorie:
                schema = GetSub_CategoriesSchema()
                data = schema.dump(categorie).data
                return data
            return ("no data is available with this id")
        except:
            raise PostFailed("call failed")

    # call to update the categorie based on id
    def put(self,id):
        try:
            categorie = db.session.query(Sub_Categories).filter(Sub_Categories.id == id).update(request.get_json())
            if categorie:
                db.session.commit()
                obj=db.session.query(Sub_Categories).filter(Sub_Categories.id==id).one()
                schema = Sub_CategoriesSchema()
                data = schema.dump(obj).data
                return data
            return("Sub-Categorie with this id is not available")
        except:
            raise PostFailed("call failed")

    # call to delete the categorie based on id
    def delete(self,id):
        try:
            obj = db.session.query(Sub_Categories).filter_by(id=id).one()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("succesfully deleted the categorie")
            return ("no category is found with this id")
        except:
            raise PostFailed("call failed")

class Sub_CategorieImageUpdate(Resource):
    def __init__(self):
        pass

    # call to update the image in categories
    def put(self,id):
        try:
            file = request.files['image']
            upload_folder = os.path.basename('/upload')
            f = os.path.join(upload_folder, file.filename)
            file.save(f)
            dit ={"image": f}
            categorie = db.session.query(Sub_Categories).filter_by(id = id).update(dit)
            if categorie:
                db.session.commit()
                obj=db.session.query(Sub_Categories).filter_by(id=id).one()
                schema = Sub_CategoriesSchema()
                data = schema.dump(obj).data
                return data
            return("categorie with this id is not available")
        except:
            raise PostFailed("call failed")
