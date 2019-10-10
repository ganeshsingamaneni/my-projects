from config import db
import datetime
from models.input_master import Input_Master


class GL_Master(db.Model):
    __tablename__ = "gl_master"
    id = db.Column(db.Integer, primary_key=True)
    gl_code = db.Column(db.String(50), nullable=False)
    gl_description = db.Column(db.Text, nullable=False)
    gl_account_category = db.Column(db.String(50), nullable=False)
    gl_nature = db.Column(db.String(50), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)
    inputmaster = db.relationship("Input_Master",
                                  backref=db.backref("input_gl"))
