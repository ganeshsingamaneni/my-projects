from config import db
import datetime


class Reel_Sheet_Ratio(db.Model):
    __tablename__ = 'reel_sheet_ratio'
    id = db.Column(db.Integer, primary_key=True)
    paper_machine_id = db.Column(db.Integer,
                                 db.ForeignKey('paper_machine_master.id'),
                                 nullable=False)
    product_code_id = db.Column(db.Integer,
                                 db.ForeignKey('product_master.id'),
                                 nullable=False)  
    mill_reel = db.Column(db.String(200),nullable =True)
    mill_sheet = db.Column(db.String(200),nullable =True)
    convertors_sheet = db.Column(db.String(200),nullable =True)
    grand_total = db.Column(db.String(200),nullable =True)
    reel_percentage = db.Column(db.String(200),nullable =True)
    mill_sheet_percentage = db.Column(db.String(200),nullable =True)
    conversion_sheet_percentage = db.Column(db.String(200),nullable =True)
    status = db.Column(db.Boolean,default = True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)
