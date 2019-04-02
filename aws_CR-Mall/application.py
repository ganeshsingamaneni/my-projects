from flask import Flask, request
# from config import *
import logging,logging.config
# from config import db
import config
from config import db
print("/////////",db)
from flask_restful import reqparse, Api,Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS
application = Flask(__name__)

class Home_page(Resource):
   def __init__(self):
      pass

   def get(self):
      return "Hiii this is ganesh singamaneni"

api = Api(application)
# CORS(app)

# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# #-------------------------------------------Roles---------------------------------------------------------------------------

from controllers.roles.post_roles import Getcreateroles
from controllers.roles.roles import GetUpdateDeleteRoles
api.add_resource(Getcreateroles, '/addrole')
api.add_resource(GetUpdateDeleteRoles, '/getupdatedelete/<int:id>')
api.add_resource(Home_page,'/')


#-------------------------------------------Users---------------------------------------------------------------------------

# from controllers.users.user_signin import Signin
# from controllers.users.user_signup import Signup
# from controllers.users.user_resetpassword import UserForget_Password,UserReset_password
# from controllers.users.user import GetUsers, GetUpdateUser, ActiveUsers
# from controllers.users.verifyemail import VerifyEmail
# from controllers.users.verifymobile import MobileVerification
# api.add_resource(Signup,'/usersignup')
# api.add_resource(Signin,'/usersignin')
# api.add_resource(VerifyEmail,'/userverifyemail/<int:id>')
# api.add_resource(MobileVerification,'/userverifymobile/<int:id>')
# api.add_resource(GetUsers,'/getallusers')
# api.add_resource(GetUpdateUser,'/getupdateuser/<int:id>')
# api.add_resource(UserReset_password,"/user_resetpassword/<int:id>")
# api.add_resource(UserForget_Password,"/user_forgetpassword")
# api.add_resource(ActiveUsers,'/activeusers')





# #-------------------------------------------Categories----------------------------------------------------------------------

# from controllers.categories.post_categories import GetcreateCategories
# from controllers.categories.categories import UpdateDeleteCategories
# from controllers.categories.getcategories import GetCategorieBy_name,GetActiveCategories
# api.add_resource(GetcreateCategories,'/getcreatecategories')
# api.add_resource(UpdateDeleteCategories,'/getupdatedeletecategories/<int:id>')
# #api.add_resource(ImageUpdate,"/updatecategoryimage/<int:id>")
# api.add_resource(GetActiveCategories,"/getactivecategories")
# api.add_resource(GetCategorieBy_name,"/getcategoriebyname/<name>")




if __name__ == "__main__":
   application.debug = True
   application.run()
# from flask import Flask

# # import config
# # from config import db

# # print(db)



# # print a nice greeting.
# def say_hello(username = "World"):
#    return '<p>Hello %s!</p>\n' % username

# # some bits of text for the page.
# header_text = '''
#    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#    <p><em>Hint</em>: Test by caratred team with db ! Append a username
#    to the URL (for example: <code>/Thelonious</code>) to say hello to
#    someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'

# # EB looks for an 'application' callable by default.
# application = Flask(__name__)

# # add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#    say_hello() + instructions + footer_text ))

# # add a rule when the page is accessed with a name appended to the site
# # URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#    header_text + say_hello(username) + home_link + footer_text))

# # run the app.
# if __name__ == "__main__":
#    # Setting debug to True enables debug output. This line should be
#    # removed before deploying a production app.
#    application.debug = True
#    application.run()
