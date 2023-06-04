"""cook URL Configuration
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('contact.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
