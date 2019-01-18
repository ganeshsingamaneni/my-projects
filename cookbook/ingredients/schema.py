import graphene
from django.shortcuts import get_object_or_404
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ingredients.models import Category, Ingredient
from graphene import ObjectType
from graphql_relay import from_global_id

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

# class CategoryInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#
# class IngredientInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     notes = graphene.String()
#     category_id = graphene.List(CategoryInput)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
    category =  graphene.Field(lambda:CategoryType)

    def mutate(root,info,name):
        category_instance = Category.objects.create(name=name)

        return CreateCategory(category = category_instance)
class categorymutation(graphene.ObjectType):
    create_category= CreateCategory.Field()

class CategoryQuery(object):
    category = graphene.Field(CategoryType,
            id = graphene.Int(),)
    all_categories = graphene.List(CategoryType)
    def resolve_all_categories(self,info,**kwargs):
        return Category.objects.all()
    def resolve_category(self,info,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None
# class UpdateCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required = True)
#         name = graphene.String()
#     category =  graphene.Field(CategoryType)
#     def mutate(root,info,id,name):
#         category_instance = Category.objects.get(id=id)
#         if category_instance:
#             category_instance.name = name
#             category_instance.save()
#             return UpdateCategory(category = category_instance)
#         return None
class UpdateCategory(graphene.Mutation):
   class Arguments:
       id = graphene.Int(required=True)
       name = graphene.String()

   ok = graphene.Boolean()
   categories = graphene.Field(CategoryType)
   def mutate(root, info, id, name):
       ok = False
       categroy_instance = Category.objects.get(id=id)
       if categroy_instance:
           ok = True
           categroy_instance.name = name
           categroy_instance.save()
           return UpdateCategory(ok=ok, categories=categroy_instance)
       return UpdateCategory(ok=ok, categories=None)
class cat_update_mutation(graphene.ObjectType):
    update_category= UpdateCategory.Field()
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    ok = graphene.Boolean()
    categories = graphene.Field(CategoryType)
    def mutate(root, info, id):
        ok = False
        categroy_instance = Category.objects.get(id=id)
        if categroy_instance:
            ok = True
            categroy_instance.delete()
            return ('success')
        return None
class delete_cat_mutation(graphene.ObjectType):
    delete_category =  DeleteCategory.Field()

class IngredientQuery(object):
    ingredient = graphene.Field(IngredientType,
        id=graphene.Int(),)
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        return None


class CreateIngredients(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String()
        notes = graphene.String()
        category_id = graphene.Int()

    def mutate(self, info, name,notes, category_id):

        category = Category.objects.get(id=category_id)
        print("xxxxx: ",category)
        ingredient = Ingredient(name=name,notes = notes, category=category)
        ingredient.save()

        return CreateIngredients(
            id=ingredient.id,
            name=ingredient.name,
            notes = ingredient.notes,
            category=category)


class IngredientMutation(graphene.ObjectType):
    create_ingredient = CreateIngredients.Field()
