from flask import Flask, request
from config import *
import logging,logging.config
from config import db
from flask_restful import reqparse, Api,Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app = Flask(__name__)
# app.wsgi_app = LoggerMiddleware(app.wsgi_app)
'''
@app.before_request
def hook():
    # request - flask.request
    lol = 'endpoint: %s, url: %s, path: %s, headers: %s, method: %s' % (request.endpoint,request.url,request.path,request.headers,request.method)
    print("==========",lol)
'''
class Home_page(Resource):
   def __init__(self):
      pass

   def get(self):
      return "Hiii"

api = Api(app)
CORS(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#-------------------------------------------Roles---------------------------------------------------------------------------

from controllers.roles.post_roles import Getcreateroles
from controllers.roles.roles import GetUpdateDeleteRoles
api.add_resource(Getcreateroles, '/addrole')
api.add_resource(GetUpdateDeleteRoles, '/getupdatedeleteroles/<int:id>')
api.add_resource(Home_page,'/')
#-------------------------------------------Permissions---------------------------------------------------------------------









if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug = True)
