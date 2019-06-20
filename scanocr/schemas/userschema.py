from config import ma,db
from models.rolemodel import Roles
from models.usermodel import User,RevokedTokenModel
from config import ma,db
from marshmallow import fields
from marshmallow.fields import Nested
from schemas.roleschema import RoleSchema


class UsersGetSchema(ma.ModelSchema):
    Roles = ma.Nested(RoleSchema)
    class Meta:
        model =User
        sqla_session = db.session

class UsersSchema(ma.ModelSchema):
    class Meta:
        models = User
        fields = ("id","first_name","last_name","role_id","email","phone","address","gender","status","created_at")
        sqla_session = db.session

class user_signupSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ("id","email","password")
        sqla_session = db.session

class Password_ResetSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ("password",)
        sqla_session = db.session


class UserlogoutSchema(ma.ModelSchema):
    class Meta:
        model = RevokedTokenModel
        sqla_session = db.session
