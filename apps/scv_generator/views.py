from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from apps.scv_generator.models import DataSchema, SchemaFieldsModel, SchemaFileModel


class ListMainPage(ListView):
    template_name = 'base/base.html'


class ListUserSchemas(ListView):
    template_name = 'csv_generator/data_schemas.html'
    model = DataSchema
    context_object_name = "data_schemas"


class CreateSchemaView(CreateView):
    model = DataSchema
    fields = []
    template_name = 'csv_generator/create_schema.html'
    success_url = reverse_lazy("localhost:8000")


class SchemaDetailView(TemplateView):
    model = SchemaFieldsModel
    template_name = 'csv_generator/schema_details.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk", None)
        schema = get_object_or_404(DataSchema.objects.all(), pk=pk)
        context = {
            'schema': schema,
            'list_fields': SchemaFieldsModel.objects.filter(
                key_schema_id=pk
            ).values(
                "order",
                "data_field_name",
                "data_type__data_type",
            ),
            'list_files': SchemaFileModel.objects.filter(data_schema_id=pk)
        }
        return self.render_to_response(context)

    # queryset = SchemaFieldsModel.objects.filter(key_schema_id=1)
