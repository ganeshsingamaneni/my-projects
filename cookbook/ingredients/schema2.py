# class Query(ObjectType):
#     category = graphene.Field(CategoryType,
#                               id=graphene.Int(),
#                               name=graphene.String())
#     all_categories = graphene.List(CategoryType)
#
#
#     ingredient = graphene.Field(IngredientType,
#                                 id=graphene.Int(),
#                                 name=graphene.String(),
#                                 notes= graphene.String(),
#                                 category_id = graphene.Int()
#                                 )
#     all_ingredients = graphene.List(IngredientType)
#
#     def resolve_all_categories(self, info, **kwargs):
#         return Category.objects.all()
#
#     def resolve_all_ingredients(self, info, **kwargs):
#         return Ingredient.objects.all()
#
#     def resolve_category(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')
#
#         if id is not None:
#             return Category.objects.get(pk=id)
#
#         if name is not None:
#             return Category.objects.get(name=name)
#         return None
#
#     def resolve_ingredient(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')
#
#         if id is not None:
#             return Ingredient.objects.get(pk=id)
#
#         if name is not None:
#             return Ingredient.objects.get(name=name)
#
#         return None
#
#
# class UpdateCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = CategoryInput(required = True)
#     ok = graphene.Boolean()
#     category = graphene.Field(CategoryType)
#
#     @staticmethod
#     def mutate(root,info,id,input=None):
#         ok =False
#         category_instance = Category.objects.get(pk=id)
#         if category_instance:
#             ok = True
#             category_instance.name = input.name
#             category_instance.save
#             return UpdateCategory(ok=ok,category = category_instance)
#         return UpdateCategory(ok = ok, category=None)
# #-------------------------------------------------------------------------
# class CreateIngredients(graphene.Mutation):
#     class Arguments:
#         input = IngredientInput(required=True)
#     ok = graphene.Boolean()
#     ingredient = graphene.Field(IngredientType)
#
#     @staticmethod
#     def mutate(root,info,input=None):
#         ok = True
#         category_id = []
#         for categories_input in input.category:
#             categor = Category.objects.get(pk=categories_input.id)
#             if categor is None:
#                 return CreateIngredients(ok=False,ingredients = None)
#             category.append(categor)
#             ingredients_instance = Ingredient(name=input.name,notes=input.notes)
#             ingredients_instance.save()
#             ingredients_instance.categories.set(category_id)
#             return CreateIngredients(ok =ok,ingredients=ingredients_instance)
#
#
# class MyMutations(graphene.ObjectType):
#     create_category = CreateCategory.Field()
#     update_category = UpdateCategory.Field()
#     create_ingredient = CreateIngredients.Field()
#
# schema = graphene.Schema(query = Query,mutation = MyMutations)
#
