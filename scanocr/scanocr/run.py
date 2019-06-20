from flask import Flask,make_response,request
import config
from config import db,app
from flask_restful import Api
import os
from middleware.middleware import LoggerMiddleware
import pathlib
from flask_cors import CORS


app.wsgi_app = LoggerMiddleware(app.wsgi_app)
api = Api(app)
CORS(app,resources={r"/vision/api/*":{"origins":"*"}})
#request.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"



app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


        #passport api calls

from app.passport.postpassport import GetPassportDetails
from app.passport.imagepost import PostImageDetail
from app.passport.getupdatedelete import GetUpdatePassport
from app.passport.testimage import ImageDetail

api.add_resource(PostImageDetail, '/vision/api/postimagedetail')
api.add_resource(GetUpdatePassport, '/vision/api/getupdatepassport/<int:id>')
api.add_resource(GetPassportDetails, '/vision/api/postpassportdetail')
api.add_resource(ImageDetail,'/vision/api/testimage')


       # aadhar api calls
from app.aadhar_scan.post_aadhar import ScanAadhar
from app.aadhar_scan.addressaadhar import ScanAddress

api.add_resource(ScanAadhar, '/vision/api/scan_aadhar')
api.add_resource(ScanAddress,'/vision/api/scanaddress')


from app.roles.postroles import Getcreateroles
from app.roles.getupdatedeleteroles import GetUpdateDeleteRoles

api.add_resource(Getcreateroles, '/vision/api/addrole')
api.add_resource(GetUpdateDeleteRoles, '/vision/api/getupdatedeleteroles/<int:id>')


            # permission api calls

from app.permission.postpermission import Getcreatepermission
from app.permission.getupdatedeletepermission import GetUpdateDeletePermission

api.add_resource(Getcreatepermission, '/vision/api/addpermission')
api.add_resource(GetUpdateDeletePermission,'/vision/api/getupdatedeletepermission/<int:id>')

   # user api calls

from app.user.user_signup import Signup
from app.user.getupdateuser import GetUsers, GetUpdateUser, ActiveUsers
from app.user.resetpassword import Forget_Password,Reset_password
from app.user.usersignin import Signin, SecretResource, UserLogoutAccess,UserLogoutRefresh

api.add_resource(Signup,'/vision/api/usersignup')
api.add_resource(Signin,'/vision/api/usersignin')
api.add_resource(GetUsers,'/vision/api/getuser')
api.add_resource(GetUpdateUser,'/vision/api/getupdateuser/<int:id>')
api.add_resource(ActiveUsers,'/vision/api/activeuser')
api.add_resource(Forget_Password,'/vision/api/forgetpassword')
api.add_resource(Reset_password,'/vision/api/resetpassword/<int:id>')
api.add_resource(SecretResource,'/vision/api/secretresource')
api.add_resource(UserLogoutAccess,'/vision/api/userlogoutaccess')
api.add_resource(UserLogoutRefresh,'/vision/api/userlogoutrefresh')




from flask_jwt_extended import JWTManager
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt = JWTManager(app)


from models import usermodel

from models.usermodel import RevokedTokenModel

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return usermodel.RevokedTokenModel.is_jti_blacklisted(jti)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
