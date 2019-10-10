from config import ma, db
from models.gl_master import GL_Master


class GLMasterSchema(ma.ModelSchema):
    class Meta:
        model = GL_Master
        sqla_session = db.session
