from config import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.category_master import Category_Master
from models.financial_year_master import Financial_Year_Master
from models.gl_master import GL_Master
from models.input_master import Input_Master
from models.pm_master import Paper_Machine_Master
from models.product_master import Product_Master
from models.profit_center_master import Profit_Center_Master
from models.sales_category_master import Sales_Category_Master
from models.segment_master import Segment_Master
from models.uom_master import UOM_Master
from models.nsr_data_information import Nsr_Data_Information
from models.reel_sheet_ratio import Reel_Sheet_Ratio
from models.time_balancing import Time_Balancing
from models.machine_production_data_information import Machine_Production_Data_Information
from models.view_model import View_Model


migrate = Migrate(app, db)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()