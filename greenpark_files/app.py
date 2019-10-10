from flask_restful import Api
from config import *
api = Api(app)
from controllers.names.post_names import Post_Outlets
from controllers.file_details.post_file_details import File_Details
api.add_resource(Post_Outlets,"/add_outlets")
api.add_resource(File_Details,"/filedetails")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)