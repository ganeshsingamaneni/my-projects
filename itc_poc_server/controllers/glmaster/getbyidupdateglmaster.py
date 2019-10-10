import datetime
from flask_restful import Resource, request
from config import *
from models.gl_master import GL_Master
from schemas.gl_master_schema import GLMasterSchema
import os
from os.path import expanduser
import logging
import logging 
import logging.config
import yaml

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/gl_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postgl_master')
loggers = logging.getLogger("gl_masterconsole")

# Getbyid, update and Delete calls
class GetbyidUpdateDelete_GL_Master(Resource):
    def __init__(self):
        pass

    # gl master get call based on id
    def get(self, id):
        try:
            get_gl = db.session.query(GL_Master).filter(
                GL_Master.id == id).first()
            if get_gl:
                schema = GLMasterSchema()
                data = schema.dump(get_gl)
                logger.info("succesfully fetched the data of this GL_Master id")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this  GL_Master id")
                return {
                    "success": False,
                    "message": "No data is found on this  GL_Master id"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # gl master update call based on id
    def put(self, id):
        try:
            gl_data = request.get_json()
            gl_data.update({"updatedAt": datetime.datetime.utcnow()})
            obj = db.session.query(GL_Master).filter(
                GL_Master.id == id).update(gl_data)
            if obj:
                db.session.commit()
                abc = db.session.query(GL_Master).filter_by(id=id).one()
                schema = GLMasterSchema()
                data = schema.dump(abc)
                logger.info("succesfully Updated data of this GL_Master id")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this  id")
                return {
                    "success": False,
                    "Meassage": "No data is found on this GL_Master id"
                }
        except Exception as e:
            logger.exception("Exception occured")        
            return {
                    "success": False,
                    "message": str(e)
                }

    # gl master delete call based on id
    def delete(self, id):
        try:
            obj = db.session.query(GL_Master).filter(
                GL_Master.id == id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("GL master deleted successfully")
                return {
                    "success": True,
                    "message": "GL master deleted successfully"
                }
            else:
                logger.info("GL master No data is found on this id")
                return ("No data is found on this id")
        except Exception as e:
            logger.exception("Exception occured")            
            return {
                    "success": False,
                    "message": str(e)
                }
