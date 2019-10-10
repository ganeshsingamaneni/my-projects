from config import db
import datetime
from models.profit_center_master import Profit_Center_Master
from models.time_balancing import Time_Balancing
from models.reel_sheet_ratio import Reel_Sheet_Ratio
from models.nsr_data_information import Nsr_Data_Information
 


class Paper_Machine_Master(db.Model):
    __tablename__ = "paper_machine_master"
    id = db.Column(db.Integer, primary_key=True)
    paper_machine_code = db.Column(db.String(50), nullable=False)
    paper_machine_name = db.Column(db.String(50), nullable=False)
    reel_percentage = db.Column(db.String(200), nullable=True)
    sheet_percentage_iss = db.Column(db.String(200), nullable=True)
    sheet_percentage_oss = db.Column(db.String(200), nullable=True)
    tph = db.Column(db.String(200), nullable=True)
    machine_hr_by_ton = db.Column(db.String(200), nullable=True)
    c_w_percentage_reel = db.Column(db.String(200), nullable=True)
    c_w_percentage_iss = db.Column(db.String(200), nullable=True)
    c_w_percentage_oss = db.Column(db.String(200), nullable=True)
    fl_percentage_reel = db.Column(db.String(200), nullable=True)
    fl_percentage_iss = db.Column(db.String(200), nullable=True)
    fl_percentage_oss = db.Column(db.String(200), nullable=True)
    replup_percentage = db.Column(db.String(200), nullable=True)
    down_time_percentage = db.Column(db.String(200), nullable=True)
    
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime)

    profit_center = db.relationship("Profit_Center_Master",
                                    backref=db.backref("paper_profit"))

    paper_machine_time_balancing = db.relationship("Time_Balancing",
                                    backref=db.backref("time_balance_paper_machine"))
    paper_machine_reel_sheet_ratio = db.relationship("Reel_Sheet_Ratio",
                                    backref=db.backref("reel_sheet_ratio_paper_machine"))  
    # paper_machine_nsr_data = db.relationship(Nsr_Data_Information,
                                    # backref=db.backref("nsr_data_paper_machine"))                                                                                              

