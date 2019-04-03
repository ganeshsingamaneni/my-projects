from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Colours
from schemas.colour import ColourSchema
from exceptions import PostFailed
import os


class GetUpdateDeleteColours(Resource):
    def __init__(self):
        pass

    # call to get the colour based on id
    def get(self,id):
        colour = db.session.query(Colours).filter(Colours.id == id).first()
        if colour:
            schema = ColourSchema()
            data = schema.dump(colour).data
            return data
        return ("no data is available with this id")

    # call to update the colour based on id
    def put(self,id):
        colour = db.session.query(Colours).filter(Colours.id == id).update(request.get_json())
        if colour:
            db.session.commit()
            obj=db.session.query(Colours).filter(Colours.id==id).one()
            schema = ColourSchema()
            data = schema.dump(obj).data
            return data
        return("colour with this id is not available")

    # call to delete the colour based on id
    def delete(self,id):
        try:
            obj = db.session.query(Colours).filter_by(id=id).one()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("succesfully deleted the colour")
            return ("no colour is found with this id")
        except:
            raise PostFailed("call failed")

class ColourImageUpdate(Resource):
    def __init__(self):
        pass

    # call to update the image in colour
    def put(self,id):
        file = request.files['image']
        upload_folder = os.path.basename('/upload')
        f = os.path.join(upload_folder, file.filename)
        file.save(f)
        dit ={"image": f}
        colour = db.session.query(Colours).filter_by(id = id).update(dit)
        if colour:
            db.session.commit()
            obj=db.session.query(Colours).filter_by(id=id).one()
            schema = ColourSchema()
            data = schema.dump(obj).data
            return data
        return("colour with this id is not available")
