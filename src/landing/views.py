from django.shortcuts import render
from django.views.generic import TemplateView
from bakery.views import BuildableTemplateView


class IndexTemplateView(BuildableTemplateView):
    template_name = 'landing/index.html'
    build_path = 'index.html'
