from django.shortcuts import render
from django.views.generic import ListView

from apps.scv_generator.models import DataSchema


# Create your views here.


class ListMainPage(ListView):
    template_name = 'base/base.html'


class ListUserSchemas(ListView):
    template_name = 'csv_generator/data_schemas.html'
    model = DataSchema
    context_object_name = "data_schemas"
