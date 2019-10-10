from config import db
import datetime


class View_Model(db.Model):
    __tablename__ = "view_model"
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(150), nullable=False)
    machineNbr = db.Column(db.String(150), nullable=False)
    distributionChannel = db.Column(db.String(150), nullable=False)
    profitCenter = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    lyplan = db.Column(db.String(150), nullable=False) 
    actualPlan = db.Column(db.String(150), nullable=False)
    bomData = db.Column(db.JSON,nullable = False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)