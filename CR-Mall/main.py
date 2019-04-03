from flask import Flask, request
from middleware import LoggerMiddleware
from config import *
import logging,logging.config
from config import db
from flask_restful import reqparse, Api,Resource
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
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

a
#-------------------------------------------Roles---------------------------------------------------------------------------


#-------------------------------------------Permissions---------------------------------------------------------------------



#-------------------------------------------Staff---------------------------------------------------------------------------


#-------------------------------------------Users---------------------------------------------------------------------------




#-------------------------------------------Banner-Image--------------------------------------------------------------------



#-------------------------------------------Categories----------------------------------------------------------------------





#-------------------------------------------Sub-Category--------------------------------------------------------------------





if __name__ == "__main__":
    app.run( debug = True)
