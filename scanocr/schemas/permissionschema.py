from models.permissionmodel import Permission
from config import ma,db
from marshmallow.fields import Nested
from schemas.roleschema import RoleSchema



class PermissionSchema(ma.ModelSchema):
    Permission = ma.Nested(RoleSchema)
    class Meta:
        model = Permission
        fields =("POST","GET","PUT","role_id","id","view_name")
        sqla_session = db.session

class GetPermissionSchema(ma.ModelSchema):
       Role_Permissions = ma.Nested(RoleSchema)
       class Meta:
           model = Permission
           sqla_session = db.session
