from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import *
from models.file_model import Output_files_Details
from models.hotel_model import Hotel_Details
from models.sac_code_model import Sac_Tran_Codes_Mapping


migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()