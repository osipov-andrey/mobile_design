from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import Application, Version, Screen, SubElement, SubPattern
from .forms import SelectElementsForm


def index(request):
    applications = Application.objects.all()
    last_versions = []
    for application in applications:
        last_version = application.last_version()
        last_versions.append(last_version)
    context = {'apps_last_version': last_versions}
    return render(request, 'main/home.html', context)


class AppPage(ListView):
    model = Screen

    def get_template_names(self):
        if 'elements' in self.kwargs:
            template_name = 'main/app_page_elements.html'
        elif 'patterns' in self.kwargs:
            template_name = 'main/app_page_patterns.html'
        else:
            template_name = 'main/app_page.html'
        return template_name

    def get_queryset(self):
        pass

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        app = Application.objects.get(name=self.kwargs['app_name'])

        version = app.last_version()

        context['main_screen'] = version.main_screen()
        screens = version.screens()
        context['app_version'] = version
        context['screens'] = screens

        if 'elements' in self.kwargs:
            context['elements'] = SubElement.objects.all()
            form = SelectElementsForm
            context['form'] = form
        elif 'patterns' in self.kwargs:
            context['patterns'] = SubPattern.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        form = SelectElementsForm(request.POST)
        if form.is_valid():
            elements = form.cleaned_data.get('Elements')
        else:
            elements = b'false'

        app = Application.objects.get(name=self.kwargs['app_name'])
        version = app.last_version()
        screens = set(version.screens().filter(elements__in=elements))
        context = {
            'screens': screens,
            'form': form,
            'main_screen': version.main_screen(),
            'app_version': version,
        }

        return render(request, 'main/app_page_elements.html', context=context)




class ScreenDetail(DetailView):
    model = Screen

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        screen = Screen.objects.get(pk=self.kwargs['pk'])
        context['screen'] = screen
        print(context)
        return context


