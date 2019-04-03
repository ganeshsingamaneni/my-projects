from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Product_Class
from schemas.product_class import Product_ClassSchema,Product_ClassGetSchema
from exceptions import PostFailed
import os


class GetUpdateDeleteProductClass(Resource):
    def __init__(self):
        pass

    # call to get the product-class based on id
    def get(self,id):
        try:
            product_class = db.session.query(Product_Class).filter(Product_Class.id == id).first()
            if product_class:
                schema = Product_ClassGetSchema()
                data = schema.dump(product_class).data
                logger.info("Product-Class data fetched succesfully based on Id")
                return data
            return ("no data is available with this id")
        except:
            raise PostFailed("call failed")

    # call to update the product-class based on id
    def put(self,id):
        try:
            categorie = db.session.query(Product_Class).filter(Product_Class.id == id).update(request.get_json())
            if categorie:
                db.session.commit()
                obj=db.session.query(Product_Class).filter(Product_Class.id==id).one()
                schema = Product_ClassSchema()
                data = schema.dump(obj).data
                return data
            return("Product-Class with this id is not available")
        except:
            raise PostFailed("call failed")

    # call to delete the product-class based on id
    def delete(self,id):
        try:
            obj = db.session.query(Product_Class).filter_by(id=id).one()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("succesfully deleted the product-class")
            return ("no product-class is found with this id")
        except:
            raise PostFailed("call failed")
class ProductClassImageUpdate(Resource):
    def __init__(self):
        pass

    # call to update the image in product-class
    def put(self,id):

        try:
            file = request.files['image']
            upload_folder = os.path.basename('/upload')
            f = os.path.join(upload_folder, file.filename)
            file.save(f)
            dit ={"image": f}
            categorie = db.session.query(Product_Class).filter_by(id = id).update(dit)
            if categorie:
                db.session.commit()
                obj=db.session.query(Product_Class).filter_by(id=id).one()
                schema = Product_ClassSchema()
                data = schema.dump(obj).data
                return data
            return("Product-Class with this id is not available")
        except:
            raise PostFailed("call failed")
