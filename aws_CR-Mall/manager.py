from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import *
from models import *
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()
db.session.commit()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
