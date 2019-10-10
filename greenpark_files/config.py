from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
# from flask_mail import Mail, Message
import os, requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://ganesh:ganesh55@localhost/greenpark_files"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ma = Marshmallow(app)
db.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ganesh1995.55@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


# def Mail_index(subject, email, body, file1, file2):
#     msg = Message(subject, sender='ganesh1995.55@gmail.com',
#                   recipients=[email])
#     msg.body = body
#     with app.open_resource(file1) as fp:
#         msg.attach(
#             "output.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", fp.read())
#     with app.open_resource(file2) as fp:
#         msg.attach("no_codes.csv", "text/csv", fp.read())
#     mail.send(msg)
#     return "Sent"


