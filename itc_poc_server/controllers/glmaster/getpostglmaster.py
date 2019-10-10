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

# Post and Get call of GL Master Model
class GetPost_GL_Master(Resource):
    def __init__(self):
        pass

    # GL Master Get call
    def get(self):
        try:
            gl = db.session.query(GL_Master).order_by(GL_Master.id).all()
            if gl:
                schema = GLMasterSchema(many=True)
                data = schema.dump(gl)
                logger.info("succesfully fetched the  GL_Master data")
                return ({"success": True, "data": data})
            else:
                logger.info("No data is available on GL_master")
                return ({
                    "success": False,
                    "message": "No data is available on GL master"
                })
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # GL Master Post call
    def post(self):
        try:
            get_data = request.get_json()
            code = get_data['gl_code']
            existing_code = GL_Master.query.filter(
                GL_Master.gl_code == code).one_or_none()
            if existing_code is None:
                schema = GLMasterSchema()
                new_gl = schema.load(get_data, session=db.session)
                db.session.add(new_gl)
                db.session.commit()
                data = schema.dump(new_gl)
                logger.info(" GL_Master succesfully posted")
                return {"success": True, "data": data}
            else:
                logger.info("GL_Master same data exists in data")
                return {
                    "success": False,
                    "message": "GL master code already exists"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }
