from graphene_django import DjangoObjectType

from blog.models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe

        fields = ('name', 'serves')
