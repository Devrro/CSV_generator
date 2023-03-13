import asyncio
import json
from typing import Any

from channels.db import database_sync_to_async

from asgiref.sync import sync_to_async

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView

from apps.scv_generator.models import DataSchema, FieldDataTypesModel, SchemaConfigsModel, SchemaFieldsModel, \
    SchemaFileModel
from apps.scv_generator.serializers import create_schema_model
from apps.scv_generator.view_helpers import generate_data_helper


class ListMainPage(ListView):
    template_name = 'base/base.html'


class ListUserSchemas(LoginRequiredMixin, ListView):
    template_name = 'csv_generator/data_schemas.html'
    model = DataSchema
    context_object_name = "data_schemas"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['data_schemas'] = context['data_schemas'].filter(user=self.request.user).order_by("-created")
        return context


class CreateSchemaView(LoginRequiredMixin, CreateView):
    model = DataSchema
    fields = []
    template_name = 'csv_generator/create_schema.html'
    success_url = reverse_lazy("list_user_schemas")

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["field_types"] = FieldDataTypesModel.objects.all().values()
        return context

    def get_success_url(self):
        return reverse_lazy("list_user_schemas")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        table_fields = json.loads(self.request.POST.get("fields"))
        table_options = json.loads(self.request.POST.get("table_options"))
        user = self.request.user
        new_schema = create_schema_model(user, table_fields, table_options)

        return HttpResponseRedirect(reverse_lazy('list_user_schemas'))


class DeleteSchemaView(LoginRequiredMixin, DeleteView):
    model = DataSchema
    queryset = DataSchema.objects.all()
    template_name = "csv_generator/dataschema_confirm_delete.html"
    success_url = reverse_lazy("list_user_schemas")


class SchemaDetailView(LoginRequiredMixin, TemplateView):
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
            'list_dialect': {
                'separator': SchemaConfigsModel.objects.get(data_schema_id=pk).get_separator_display(),
                'string_character': SchemaConfigsModel.objects.get(data_schema_id=pk).get_string_character_display()
            },
            'list_files': SchemaFileModel.objects.filter(data_schema_id=pk).order_by("-created")
        }
        return self.render_to_response(context)


async def async_view(request, *args, **kwargs):
    rows = int(request.POST.get("count_of_rows"))
    schema_fields_id = kwargs.get("pk")
    create_db_record = database_sync_to_async(SchemaFileModel.objects.create)
    schema_model = await create_db_record(data_schema_id=schema_fields_id)

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(
    await sync_to_async(
        generate_data_helper
    )(rows, schema_model, schema_fields_id, *args, **kwargs)
    # )

    payload = json.dumps({
        "type": "file_record_created",
        "text": {
            "schema_id": schema_model.id,
            "is_generated": schema_model.is_generated,
            "created": str(schema_model.created),
            "csv_file": str(schema_model.csv_file),
        }})
    return HttpResponse(content=payload)
