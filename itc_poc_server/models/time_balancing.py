from config import db
import datetime


class Time_Balancing(db.Model):
    __tablename__ = 'time_balancing'
    id = db.Column(db.Integer, primary_key=True)
    work_center_code = db.Column(db.Integer,
                                 db.ForeignKey('paper_machine_master.id'),
                                 nullable=False)
    profit_center_code = db.Column(db.Integer,
                                 db.ForeignKey('product_master.id'),
                                 nullable=False) 
    tones_per_hour = db.Column(db.String(200),nullable =True)
    machine_hour_per_tonnage = db.Column(db.String(200),nullable =True)
    wrapper_reel_percentage = db.Column(db.String(200),nullable =True)
    wrapper_mill_sheet_percentage = db.Column(db.String(200),nullable =True)
    wrapper_converter_sheet_percentage = db.Column(db.String(200),nullable =True)
    finishing_loss_reel_percentage = db.Column(db.String(200),nullable =True)
    finishing_loss_mill_sheet_percentage = db.Column(db.String(200),nullable =True)
    finishing_loss_converter_percentage = db.Column(db.String(200),nullable =True)
    down_time_percentage = db.Column(db.String(200),nullable =True)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)                                                         