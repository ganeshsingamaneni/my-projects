from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import *
from models.file_details import Files_Details
from models.names_model import Outlet_Details
# from models.sac_codes import Sac_Tran_Codes_Mapping
# from models.users import Users


migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()