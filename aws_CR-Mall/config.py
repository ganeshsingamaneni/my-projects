import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mysqldb import MySQL

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'MySQL',
            'NAME': os.environ['mall'],
            'USER': os.environ['root'],
            'PASSWORD': os.environ['caratred'],
            'HOST': os.environ['crmall.cwmz2iydy0hy.us-east-2.rds.amazonaws.com'],
            'PORT': os.environ['3306'],
        }
    }
    SQLALCHEMY_DATABASE_URI = 'mysql://'+ DATABASES['default']['USER'] +':'+ DATABASES['default']['PASSWORD'] +'@'+ DATABASES['default']['HOST']+':'+DATABASES['default']['PASSWORD'] + '/'+ DATABASES['default']['NAME']

else:
    SQLALCHEMY_DATABASE_URI ="mysql://root:caratred@crmall.cwmz2iydy0hy.us-east-2.rds.amazonaws.com/mall"


# SQLALCHEMY_DATABASE_URI ="mysql://prasant:Welcome123@scanocr.cwmz2iydy0hy.us-east-2.rds.amazonaws.com/scanocr"

connex_app = connexion.App(__name__)
app = connex_app.app

mysql = MySQL()

# SQLALCHEMY_DATABASE_URI = 'mysql://root:Welcome@123@104.199.146.29/training_fraud'

app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config[]



db = SQLAlchemy(app)
ma = Marshmallow(app)