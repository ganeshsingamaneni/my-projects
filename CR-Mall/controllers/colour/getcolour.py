from datetime import datetime
from flask_restful import Resource
from config import db
from models import Colours
from schemas.colour import ColourSchema


class GetActiveColours(Resource):
    def __init__(self):
        pass

    def get(self):
        # call to get the active product_class
        colour = db.session.query(Colours).filter(Colours.status == True).all()
        if colour:
            schema = ColourSchema()
            data = schema.dump(colour,many=True).data
            return data
        return("No colour with such status")

class GetColourByProduct(Resource):
    def __init__(self):
        pass

    # call to get the sizes by category
    def get(self,id):
        colour = db.session.query(Colours).filter(Colours.product_id == id).all()
        if colour:
            schema = ColourSchema()
            data = schema.dump(colour, many=True).data
            return data
        return("no colour with such product")
