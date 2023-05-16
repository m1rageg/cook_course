from allauth.account.views import LogoutView
from django.urls import path, include

from blog.auth_views import login_view, logout_view
from . import views


urlpatterns = [
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('feedback/', views.CreateContact.as_view(), name="feedback"),
    path("accounts/", include("allauth.urls")),
    path("logout", LogoutView.as_view()),
    path("api/login", login_view),
    path("api/logout", logout_view),
]
