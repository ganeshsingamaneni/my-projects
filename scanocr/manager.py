from flask import Flask
import logging,logging.config
import os
from models.persondetails import Passport_Details
from models.permissionmodel import Permission
from models.rolemodel import Roles
from models.usermodel import User, RevokedTokenModel
from models.scandetaillog import Detailslog

from flask_restful import Api
from config import db,app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand




app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])


migrate = Migrate(app, db)

app.app_context().push()

db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
