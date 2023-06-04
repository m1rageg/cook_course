import graphene

from blog.models import Recipe
from blog.schema import RecipeType


class Query(graphene.ObjectType):
    recipe = graphene.List(RecipeType)

    def resolve_recipes(self, info):
        return Recipe.objects.all()


schema = graphene.Schema(query=Query)
