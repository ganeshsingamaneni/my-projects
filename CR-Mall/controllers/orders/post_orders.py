from models import Orders
from schemas.orders import OrdersSchema
from flask import request, Flask
from flask_restful import Resource
from config import *




class GetCreateOrders(Resource):
    def __init__(self):
        pass

    # call to get all the orders in list
    def get(self):
        order = db.session.query(Orders).order_by(Orders.id).all()
        if order:
            schema = OrdersSchema(many = True)
            data = schema.dump(order).data
            return data
        else:
            return("No orders found")

    # This Call is user to Add the orders
    def post(self):
        data = request.get_json()
        dit = {key:value for key,value in data.items()}
        schema = OrdersSchema()
        new_order = schema.load(dit, session=db.session,partial =True).data
        if new_order:
            db.session.add(new_order)
            db.session.commit()
            data = schema.dump(new_order).data
            return data
        else:
            return ("post call failed to add the data")
