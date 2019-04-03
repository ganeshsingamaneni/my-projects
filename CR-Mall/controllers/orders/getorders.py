from models import Orders
from schemas.orders import OrdersSchema
from flask import request, Flask
from flask_restful import Resource
from config import *


class GetOrderByUser(Resource):
    def __init__(self):
        pass

    # call to get the orders based on user id
    def get(self,id):
        order = db.session.query(Orders).filter_by(user_id=id).all()
        if order:
            schema = OrdersSchema(many = True)
            data = schema.dump(order).data
            return data
        else:
            return("No orders found based on this user id")

class GetOrderByCart(Resource):
    def __init__(self):
        pass

    # call to get the orders based on cart id
    def get(self,id):
        order = db.session.query(Orders).filter_by(cart_id=id).one()
        if order:
            schema = OrdersSchema()
            data = schema.dump(order).data
            return data
        else:
            return("No orders found based on this cart id")


class GetOrderByStatus(Resource):
    def __init__(self):
        pass

    # call to get the orders based on status
    def get(self,status):
        order = db.session.query(Orders).filter_by(order_status = status).all()
        if order:
            schema = OrdersSchema(many = True)
            data = schema.dump(order).data
            return data
        else:
            return("No orders found based on this status")
