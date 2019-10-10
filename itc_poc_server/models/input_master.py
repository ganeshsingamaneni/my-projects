from config import db
import datetime
from models.nsr_data_information import Nsr_Data_Information

class Input_Master(db.Model):
    __tablename__ = "input_master"
    id = db.Column(db.Integer, primary_key=True)
    category_code_id = db.Column(db.Integer(),
                                 db.ForeignKey('category_master.id'),
                                 nullable=False)
    sap_code = db.Column(db.String(50), nullable=False)
    sap_description = db.Column(db.Text, nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    uom_id = db.Column(db.Integer(),
                       db.ForeignKey('uom_master.id'),
                       nullable=False)
    rate = db.Column(db.String(35), nullable=False)
    gl_id = db.Column(db.Integer(),
                      db.ForeignKey('gl_master.id'),
                      nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    # input_master_nsr_data = db.relationship("Nsr_Data_Information",
    #                               backref=db.backref("nsr_data_input_master"))