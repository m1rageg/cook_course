
from django.views import View
from django.views.generic import CreateView

from .models import ContactLink, About
from .forms import ContactForm


from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})


@api_view(http_method_names=["POST"])
@authentication_classes([])
@permission_classes([])
def session_auth(request: Request):
    data = request.data

    user = authenticate(username=data["username"], password=data["password"])

    if user:
        login(request, user)
        return Response(user.username)
    else:
        return Response("Unauthorized", status=401)


