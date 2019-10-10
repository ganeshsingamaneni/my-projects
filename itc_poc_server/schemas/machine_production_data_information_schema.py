from models.machine_production_data_information import Machine_Production_Data_Information
from config import ma, db



# class Nsr_Data_Information_Schema(ma.ModelSchema):

#     class Meta:
#         model = Nsr_Data_Information
#         fields = ("master_product_id","segment_id","paper_machine_id","last_fy_nsr_value","updatedAt")
#         sqla_session = db.session

class Machine_Production_Data_Information_Schema(ma.ModelSchema):

    class Meta:
        model = Machine_Production_Data_Information
        sqla_session = db.session

class Machine_Production_Data_Information_Get_schema(ma.ModelSchema):
    # nsr_data_financial_year = ma.Nested(Financial_Year_Master_Get_schema)
    # nsr_data_input_master = ma.Nested(Input_Master_Get_schema)
    # nsr_data_segment = ma.Nested(Segment_Master_Get_schema)
    # nsr_data_paper_machine = ma.Nested(PMMasterSchema)

    class Meta:
        model = Machine_Production_Data_Information
        # fields = ('paper_machine_id','product_id','profit_center_id','segment_id','sales_category_id','Qty_Apr','Qty_May','Qty_Jun','Qty_Jul','Qty_Aug','Qty_Sep','Qty_Oct','Qty_Nov','Qty_Dec','Qty_Jan','Qty_Feb','Qty_Mar','Qty_Total',
        #             'NSR_Apr','NSR_May','NSR_Jun','NSR_Jul','NSR_Aug','NSR_Sep','NSR_Oct','NSR_Nov','NSR_Dec','NSR_Jan','NSR_Feb','NSR_Mar','NSR_Total','NSR_Value_Apr','NSR_Value_May','NSR_Value_Jun','NSR_Value_Jul','NSR_Value_Aug',
        #             'NSR_Value_Sep','NSR_Value_Oct','NSR_Value_Nov','NSR_Value_Dec','NSR_Value_Jan','NSR_Value_Feb','NSR_Value_Mar','NSR_Value_Total')
        sqla_session = db.session