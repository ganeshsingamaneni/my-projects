from models.persondetails import Passport_Details
from config import ma,db
from marshmallow_sqlalchemy import field_for

class PassportSchema(ma.ModelSchema):
    class Meta:
        model = Passport_Details
        sqla_session = db.session



class GetPassportSchema(ma.ModelSchema):

    class Meta:
        model = Passport_Details
        fields =("FamilyName","Nationality","Date_of_Birth","Visa_Number","Visa_Place_Issue","Employed_In_India","Visit_Purpose","Passport_Document_Type",
         "Phone_Number","Nationality_by_Birth","Address","Duration_of_stay_india" ,"Given_Name","Passport_Document_No",
        "Place_of_issue","Visa_Issue_Date","Visa_Type","Arrival_Date","Duration_of_stay","Arriving_From","Email","Arrived_From_Port",
        "Room_No","Registration_No","RFID_Room_Key","Gender","Date_of_Issue","Date_of_Expiry","Visa_Expiry_Date","Visa_No_Of_Enteries",
        "Arrive_Time"
        ,"Date_Arrival_in_India"
        ,"Next_Destination"
        ,"Arrived_at"
        ,"Native_COuntry_Add"
        ,"Parcentage"
        ,"Adults_in_Room"
        ,"Passport_Image")
        sqla_session = db.session
