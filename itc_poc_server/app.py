from controllers.category_masters.add_category_masters import Add_New_Category_Master,Category_Master_Details_By_Id
from controllers.profit_center_master.add_profit_center_master import Add_Profit_center_Master, Profit_Center_Master_Details_By_Id
from flask import Flask
from flask_restful import Api
from config import *


from config import *
api = Api(app)

api.add_resource(Add_New_Category_Master, "/addcategorymaster")
api.add_resource(Category_Master_Details_By_Id,"/categorymasterdetailsbyid/<int:id>")
api.add_resource(Profit_Center_Master_Details_By_Id,"/profitcentermasterdetailsbyid/<int:id>")
api.add_resource(Add_Profit_center_Master,"/addprofitcentermaster")


from controllers.pmmaster.getpostpmmaster import GetPostPMMaster
from controllers.pmmaster.getbyidupdatepmmaster import GetbyidUpdateDeletePMMaster
api.add_resource(GetPostPMMaster, '/getpostpmmaster')
api.add_resource(GetbyidUpdateDeletePMMaster,
                 '/getupdatedeletepmmaster/<int:id>')


from controllers.productmaster.getpostproducts import GetPostProductMaster
from controllers.productmaster.getbyidupdateproducts import GetbyidUpdateDeleteProductMaster
api.add_resource(GetPostProductMaster, '/getpostproducts')
api.add_resource(GetbyidUpdateDeleteProductMaster, '/getupdatedeleteproducts/<int:id>')

from controllers.uom_masters.add_uom_masters import Add_New_Uom_Master,Uom_Master_Details_By_Id

api.add_resource(Uom_Master_Details_By_Id,"/uommasterdetailsbyid/<int:id>")
api.add_resource(Add_New_Uom_Master,"/adduommaster")

from controllers.input_master.add_input_master import Add_Input_Master,Input_Master_Details_By_Id
api.add_resource(Input_Master_Details_By_Id,"/inputmasterdetailsbyid/<int:id>")
api.add_resource(Add_Input_Master,"/addinputmasters")



from controllers.glmaster.getpostglmaster import GetPost_GL_Master
from controllers.glmaster.getbyidupdateglmaster import GetbyidUpdateDelete_GL_Master
api.add_resource(GetPost_GL_Master, '/getpostmastergl')
api.add_resource(GetbyidUpdateDelete_GL_Master,
                 '/getupdatedeletemastergl/<int:id>')

from controllers.financial_year_master.add_financial_year_master import Add_New_Financial_year_Master,Financial_year_Master_Details_By_Id
api.add_resource(Financial_year_Master_Details_By_Id,"/financialyearmasterdetailsbyid/<int:id>")
api.add_resource(Add_New_Financial_year_Master,"/addnewfinancialyearmaster")


from controllers.sales_category_master.add_sales_category_master import Add_New_Sales_Category_Master,Sales_Category_Master_Details_By_Id
api.add_resource(Sales_Category_Master_Details_By_Id,"/salescategorymasterdetailsbyid/<int:id>")
api.add_resource(Add_New_Sales_Category_Master,"/addsalescategorymaster")

from controllers.segment_master.add_segment_master import Add_New_Segment_Master,Segment_Master_Details_By_Id
api.add_resource(Add_New_Segment_Master,"/addsegmentmaster")
api.add_resource(Segment_Master_Details_By_Id,"/segmentmasterdetailsbyid/<int:id>")


from controllers.machine_production.getmachine_raw_data import Get_machine_raw_data
api.add_resource(Get_machine_raw_data,"/machinerawdata/<int:id>")


from controllers.time_balancing.add_time_balancing import Add_New_Time_Balance,Time_Balancing_By_Id
api.add_resource(Time_Balancing_By_Id,"/timebalancebyid/<int:id>")
api.add_resource(Add_New_Time_Balance,"/addnewtimebalance")

from controllers.reel_sheet_ratio.add_reel_sheet_ratio import Add_Reel_Sheet_Ratio,Reel_Sheet_Ratio_By_Id
api.add_resource(Reel_Sheet_Ratio_By_Id,"/reelsheetratiobyid/<int:id>")
api.add_resource(Add_Reel_Sheet_Ratio,"/addreelsheetratio")

from controllers.nsr_data_information.add_nsr_data_information import Add_Nsr_Data_Information,Nsr_Data_Information_By_Id
api.add_resource(Nsr_Data_Information_By_Id,"/nsrdatainformationbyid/<int:id>")
api.add_resource(Add_Nsr_Data_Information,"/addnsrdatainformation")

from controllers.nsr_data_information.get_data import Get_Nsr_excel
api.add_resource(Get_Nsr_excel,"/getnsrexcel")

from controllers.profit_center_master.add_profit_center_master import Profit_Center_Master_Details_By_Paper_Machine_Id
api.add_resource(Profit_Center_Master_Details_By_Paper_Machine_Id,"/profitcenterdetailsbypapermachineid/<int:id>")

from controllers.productmaster.getbyidupdateproducts import Product_Master_Details_By_Profit_Center_Id
api.add_resource(Product_Master_Details_By_Profit_Center_Id,"/productmasterdetailsbasedonprofitcenterid/<int:id>")

from controllers.machine_production_data_information.add_machine_production import Add_Machine_Production_Data_Information, Machine_Production_Data_Information_By_Id
api.add_resource(Machine_Production_Data_Information_By_Id,"/machineproductiondatainformationbyid/<int:id>")
api.add_resource(Add_Machine_Production_Data_Information,"/addmachineproductiondatainformation")

from controllers.machine_production_data_information.get_data import Get_Machine_Production_excel
api.add_resource(Get_Machine_Production_excel,"/getmachineproductionexcel")

from controllers.time_balancing_raw_data.time_balancing_raw_data import GetTimeBalancing
api.add_resource(GetTimeBalancing,'/timebalancingrawdata/<int:id>')

from controllers.output_time_balancing.get_data import Get_time_balancing_output_excel
api.add_resource(Get_time_balancing_output_excel,"/gettimebalancexcel")

from controllers.view_model.add_view_data import Add_view_data,View_data_By_Id
from controllers.view_model.get_data import Get_View_Model_excel
api.add_resource(View_data_By_Id,"/viewdatabyid/<int:id>")
api.add_resource(Add_view_data,"/addviewdata")
api.add_resource(Get_View_Model_excel,"/getviewexcel")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
