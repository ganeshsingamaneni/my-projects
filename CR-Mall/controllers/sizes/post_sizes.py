from datetime import datetime
from flask import make_response,abort,request
from models import Sizes
from schemas.size import SizesSchema,SizesGetSchema
from sqlalchemy import and_
from config import db
from flask_restful import reqparse, abort, Api, Resource
from exceptions import Nodata,PostFailed
parser = reqparse.RequestParser()


class GetcreateSizes(Resource):
    def __init__(self):
        pass

    # Sizes get call
    def get(self):
        try:
            size = db.session.query(Sizes).order_by(Sizes.id).all()
            if size:
                size_schema = SizesSchema(many=True)
                data = size_schema.dump(size).data
                return data
            else:
                return("no data is available on sizes")
        except:
            raise Nodata("no data is available")

    # Sizes post call
    def post(self):
        da = request.get_json()
        size = da['size']
        product_id = da['product_id']
        dit = {key:value for key,value in da.items()}
        existing_size = db.session.query(Sizes).filter(and_(Sizes.product_id == product_id, Sizes.size == size)).first()
        if existing_size is None:
            schema = SizesSchema()
            new_size = schema.load(dit, session=db.session).data
            db.session.add(new_size)
            db.session.commit()
            data = schema.dump(new_size).data
            return data, 201
        else:
            return("size with this product already exist")
