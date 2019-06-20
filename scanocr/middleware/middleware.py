from flask import request
from config import *
import json
import re
from werkzeug.wrappers import Request, Response
from sqlalchemy import and_
from models.usermodel import User
from models.permissionmodel import Permission

class LoggerMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        request = Request(environ)
        #print("request body",r)
        #print("+++++++++++++",'path: %s, url: %s, headers: %s, method: %s' % (request.path, request.url, request.headers, request.method))
        path = ('%s' % (request.path))
        digit = re.findall(r'\d+', path)


        if digit == []:
            l = ['/vision/api/addrole','/vision/api/usersignin','/vision/api/addpermission','/vision/api/usersignup','/vision/api/getuser','/vision/api/userlogoutaccess','/vision/api/testimage','/vision/api/scan_aadhar','/vision/api/scanaddress','/vision/api/postimagedetail']
        else:
            dig = digit[0]
            l = ['/vision/api/getupdatedeletepermission/'+dig,'/vision/api/getupdatedeleteroles/'+dig,'/vision/api/getupdateuser/'+dig]
        #print(digit)
        if path in l:
            return self.app(environ, start_response)
        else:
            #Id = request.headers.get('id')
            Id = 1


            if digit == []:
                path1 = ('%s' % (request.path))
                query = db.session.query(User).filter(User.id == Id).first()
                role_obj = query.__dict__
                role = role_obj['role_id']
                permissions = db.session.query(Permission).filter(Permission.role_id == role,Permission.view_name == path1).first()
                #print("==========================",permissions)
                permission_obj = permissions.__dict__
                call = ('%s' % (request.method))
                if permission_obj[call] != True:
                    text = {'error':False}
                    response = Response(json.dumps({
                        'error':False,
                        'message':'error',
              }))
                else:
                    return self.app(environ, start_response)

            else:
                dig = digit[0]
                path1 = path.rstrip('/'+dig)
                #print("/////////////////: ",path1)
                query = db.session.query(User).filter(User.id == Id).first()
                role_obj = query.__dict__
                role = role_obj['role_id']
                permissions = db.session.query(Permission).filter(Permission.role_id == role,Permission.view_name == path1).first()
                #print("==========================",permissions)
                permission_obj = permissions.__dict__
                call = ('%s' % (request.method))
                if permission_obj[call] != True:
                    text = {'error':False}
                    response = Response(json.dumps({
                        'error':False,
                        'message':'error',
                    }))
                else:
                    return self.app(environ, start_response)

        return response(environ, start_response)
