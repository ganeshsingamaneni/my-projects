from config import *
import datetime

class Schedularlogs(db.Model):
    __tablename__ = "schedularlogs"
    id       = db.Column(db.Integer, primary_key = True)
    utilname = db.Column(db.String(255), nullable = True)
    status   = db.Column(db.String(255), nullable = True)
    jobstatus = db.Column(db.String(255), nullable = True)
    startTime = db.Column(db.DateTime, default = datetime.datetime.utcnow(), nullable = True)
    endTime   = db.Column(db.DateTime, default = datetime.datetime.utcnow(), nullable = True)
    timeTaken = db.Column(db.String(255), nullable = True)
    errorLogFileLocation = db.Column(db.String(225), nullable = True)
    successLogFileLocation = db.Column(db.String(225), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())


class Mocktable(db.Model):
    __tablename__= "mocktable"
    id   = db.Column(db.Integer, primary_key = True)
    fact_amount = db.Column(db.Numeric(10,2))
    fact_bank_account_num = db.Column(db.String(255), nullable = True)
    fact_bank_id = db.Column(db.String(255), nullable = True)
    fact_created_date = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    fact_pay_group = db.Column(db.String(255), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())

class Transpayment(db.Model):
   __tablename__ = "transpayment"
   id = db.Column(db.Integer, primary_key = True)
   BankAccountNo = db.Column(db.Integer)
   BankAccountName = db.Column(db.String(255))
   CommonPersonBank = db.Column(db.Boolean, default = True)
   CommonPersonBankName = db.Column(db.String(255), nullable = True)
   Donation = db.Column(db.Boolean, nullable = True)
   RecipientCount = db.Column(db.Integer)
   Reference_number = db.Column(db.String(255))
   Updated = db.Column(db.Boolean, default = True)
   UpdatedDate = db.Column(db.DateTime)
   CreatedBy = db.Column(db.String(255))
   CreatedOn = db.Column(db.DateTime, default = datetime.datetime.utcnow())
   UpdatedBy = db.Column(db.String(255))
   UpdatedOn = db.Column(db.DateTime, default = datetime.datetime.utcnow())
