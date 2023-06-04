from django_filters import FilterSet, CharFilter

from blog.models import Recipe


class RecipeFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    name_starts = CharFilter(field_name='name', lookup_expr='startswith')
    class Meta:
        model = Recipe
        fields = ['name']