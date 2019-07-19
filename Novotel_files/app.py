from flask import Flask
from flask_restful import Api
from config import *
api = Api(app)
# app.route('/html/path:path')
# def send_html(path):
#     return send_from_directory('static', path)
import json   
from controllers.sac_code_mapping.sac_map import Post_Sac_Codes
api.add_resource(Post_Sac_Codes,"/post_sac_codes")
from controllers.hotel_details.hotel_post import Post_Hotel_Details,Hotel_Details_by_id,Login
api.add_resource(Login,"/login")
api.add_resource(Post_Hotel_Details,"/post_hotel_details")
api.add_resource(Hotel_Details_by_id,"/hotel_details_byid/<int:id>")
from controllers.file_running_deatils.file_post import File_Details,Data_between_dates
api.add_resource(Data_between_dates,"/databetweendates/<start>/<end>")
api.add_resource(File_Details,"/file_details")
from controllers.file_running_deatils.show_files import File_display_excel,File_display_csv
api.add_resource(File_display_excel,"/excel_file/<par_date>")
api.add_resource(File_display_csv,"/csv_file/<par_date>")




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
