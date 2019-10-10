from models.category_master import Category_Master
from config import ma, db


class Category_Master_schema(ma.ModelSchema):

    class Meta:
        model = Category_Master
        fields = ("category_code","category_name","updated_at")
        sqla_session = db.session



class Category_Master_Get_schema(ma.ModelSchema):

    class Meta:
        model = Category_Master
        sqla_session = db.session
