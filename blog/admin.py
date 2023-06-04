from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models
from .models import Post


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class CustomPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.unregister(Post)
admin.site.register(Post, CustomPostAdmin)