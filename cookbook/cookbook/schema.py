import graphene

import ingredients.schema


class Query(
            ingredients.schema.CategoryQuery,
            ingredients.schema.IngredientQuery,
            graphene.ObjectType
           ):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to our project
    """
    pass


class Mutation(
                ingredients.schema.categorymutation,
                ingredients.schema.IngredientMutation,
                ingredients.schema.cat_update_mutation,
                ingredients.schema.delete_cat_mutation,
                graphene.ObjectType
              ):
    """
    This class will inherit from multiple Mutations
    as we begin to add more apps to our project
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
