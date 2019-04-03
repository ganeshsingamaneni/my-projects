from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Categories
from schemas.categories import CategoriesSchema, CategoryGetSchema
from exceptions import PostFailed
import os


class UpdateDeleteCategories(Resource):
    def __init__(self):
        pass

    # call to get the categorie based on id
    def get(self,id):
        try:
            categorie = db.session.query(Categories).filter(Categories.id == id).first()
            if categorie:
                schema = CategoryGetSchema()
                data = schema.dump(categorie).data
                return data
            else:
                return ("Category does not exists")
        except:
            raise PostFailed("call failed")

    # call to update the categorie based on id
    def put(self,id):
        categorie = db.session.query(Categories).filter(Categories.id == id).update(request.get_json())
        if categorie:
            db.session.commit()
            obj=db.session.query(Categories).filter(Categories.id==id).one()
            schema = CategoriesSchema()
            data = schema.dump(obj).data
            return data
        else:
            return("categorie with this id is not available")

    # call to delete the categorie based on id
    def delete(self,id):
        try:
            obj = db.session.query(Categories).filter_by(id=id).one()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("succesfully deleted the categorie")
            else:
                return ("Category does not exists")
        except:
            raise PostFailed("call failed")

'''
class ImageUpdate(Resource):
    def __init__(self):
        pass

    # call to update the image in categories
    def put(self,id):
        file = request.files['image']
        upload_folder = os.path.basename('/upload')
        f = os.path.join(upload_folder, file.filename)
        file.save(f)
        dit ={"image": f}
        categorie = db.session.query(Categories).filter_by(id = id).update(dit)
        if categorie:
            db.session.commit()
            obj=db.session.query(Categories).filter_by(id=id).one()
            schema = CategoriesSchema()
            data = schema.dump(obj).data
            logger.info("Category image updated succesfully")
            return data
        else:
            logger.warning("Category does not exists")
            return("categorie with this id is not available")

'''
