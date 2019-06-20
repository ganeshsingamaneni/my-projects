import os
from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import datetime
from sqlalchemy.orm import validates
from models.scandetaillog import Detailslog




class Passport_Details(db.Model):
    __tablename__ = "passport_details"
    id                     = db.Column(db.Integer,primary_key=True)
    FamilyName             = db.Column(db.String(50),nullable=True)
    Nationality            = db.Column(db.String(50),nullable=True)
    Date_of_Birth          = db.Column(db.String(50),nullable=True)
    Visa_Number            = db.Column(db.Integer,unique=True,nullable=True)
    Visa_Place_Issue       = db.Column(db.String(50),nullable=True)
    Employed_In_India      = db.Column(db.Enum('Yes','No'),default='NO')
    Visit_Purpose          = db.Column(db.String(50),nullable=True)
    Passport_Document_Type = db.Column(db.String(50),nullable=True)
    Phone_Number           = db.Column(db.String(50),nullable=True)
    Nationality_by_Birth   = db.Column(db.String(50),nullable=True)
    Address                = db.Column(db.Text(),nullable=True)
    Duration_of_stay_india = db.Column(db.Enum('Yes','No'),default='NO')
    Given_Name             = db.Column(db.String(50),nullable=True)
    Place_of_issue         = db.Column(db.String(50),nullable=True)
    Visa_Issue_Date        = db.Column(db.String(50),nullable=True)
    Visa_Type              = db.Column(db.String(50),nullable=True)
    Arrival_Date           = db.Column(db.String(50),nullable=True)
    Duration_of_stay       = db.Column(db.String(50),nullable=True)
    Arriving_From          = db.Column(db.String(50),nullable=True)
    Email                  = db.Column(db.String(50),nullable=True)
    Arrived_From_Port      = db.Column(db.String(50),nullable=True)
    Room_No                = db.Column(db.Integer,nullable=True)
    Registration_No        = db.Column(db.Integer,nullable=True)
    RFID_Room_Key          =  db.Column(db.Integer,nullable=True)
    Gender                 = db.Column(db.String(50),nullable=True)
    Date_of_Issue          = db.Column(db.String(50),nullable=True)
    Date_of_Expiry         = db.Column(db.String(50),nullable=True)
    Visa_Expiry_Date       = db.Column(db.String(50),nullable=True)
    Visa_No_Of_Enteries    = db.Column(db.Integer,nullable=True)
    Arrive_Time            = db.Column(db.String(50),nullable=True)
    Date_Arrival_in_India  = db.Column(db.String(50),nullable=True)
    Next_Destination       = db.Column(db.String(50),nullable=True)
    Arrived_at             = db.Column(db.String(50),nullable=True)
    Native_COuntry_Add     = db.Column(db.String(50),nullable=True)
    Parcentage             = db.Column(db.String(50),nullable=True)
    Adults_in_Room         = db.Column(db.Enum('yes','No'),default='NO')
    Passport_Image         = db.Column(db.LargeBinary, nullable = True)
    created_at             = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at             = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    Passport_Document_No   = db.Column(db.String(50),nullable=True)
    detail                 = db.relationship("Detailslog", backref = db.backref("person"))
