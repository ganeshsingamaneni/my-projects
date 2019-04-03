from models import Orders
from schemas.orders import OrdersSchema
from flask import request, Flask
from flask_restful import Resource
from config import *



class GetDeleteOrders(Resource):
    def __init__(self):
        pass

    # call to get the orders based on id
    def get(self,id):
        order = db.session.query(Orders).filter_by(id =id).first()
        if order:
            schema = OrdersSchema()
            data = schema.dump(order).data
            return data
        else:
            return("No orders found based on this id")

    #This call is user to Delete the Orders
    def delete(self,id):
        obj = db.session.query(Orders).filter_by(id = id).first()
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return ("order deleted successfully")
        else:
            return ("No order is available")
