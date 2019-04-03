from datetime import datetime
from flask_restful import Resource
from config import db
from models import Sizes
from schemas.size import SizesSchema


class GetActiveSizes(Resource):
    def __init__(self):
        pass

    # call to get the active sizes
    def get(self):
        sizes = db.session.query(Sizes).filter(Sizes.status == True).all()
        if sizes:
            schema = SizesSchema()
            data = schema.dump(sizes,many=True).data
            return data
        return("No sizes with such status")

class GetSizesBy_name(Resource):
    def __init__(self):
        pass

    # call to get the sizes by name
    def get(self,size):
        sizes = db.session.query(Sizes).filter(Sizes.size == size).all()
        if sizes:
            schema = SizesSchema()
            data = schema.dump(sizes,many=True).data
            return data
        return("no sizes with such size")

class GetSizesByProduct(Resource):
    def __init__(self):
        pass

    # call to get the sizes by category
    def get(self,id):
        sizes = db.session.query(Sizes).filter(Sizes.product_id == id).all()
        if sizes:
            schema = SizesSchema()
            data = schema.dump(sizes,many=True).data
            return data
        return("no sizes with such product")
