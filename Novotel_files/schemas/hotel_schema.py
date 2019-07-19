from models.hotel_model import Hotel_Details
from config import ma,db

class Hotel_Details_Schema(ma.ModelSchema):
    class Meta:
        model = Hotel_Details
        sqla_session = db.session