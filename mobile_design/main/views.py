from django.shortcuts import render

# Create your views here.
from .models import Application


def index(request):
    applications = Application.objects.all()
    last_versions = []
    for application in applications:
        last_version = application.last_version()
        last_versions.append(last_version)
    context = {'apps_last_version': last_versions}
    return render(request, 'main/home.html', context)