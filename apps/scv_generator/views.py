import asyncio
import json

from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from apps.scv_generator.models import DataSchema, FieldDataTypesModel, SchemaConfigsModel, SchemaFieldsModel, \
    SchemaFileModel
from apps.scv_generator.serializers import create_schema_model
from apps.scv_generator.services_generator import create_csv_file

from apps.scv_generator.consumers import FileProcessingConsumer


class ListMainPage(ListView):
    template_name = 'base/base.html'


class ListUserSchemas(LoginRequiredMixin, ListView):
    template_name = 'csv_generator/data_schemas.html'
    model = DataSchema
    context_object_name = "data_schemas"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['data_schemas'] = context['data_schemas'].filter(user=self.request.user)
        return context


class CreateSchemaView(LoginRequiredMixin, CreateView):
    model = DataSchema
    fields = []
    template_name = 'csv_generator/create_schema.html'
    success_url = reverse_lazy("localhost:8000")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_types"] = FieldDataTypesModel.objects.all().values()
        return context

    def post(self, request, *args, **kwargs):
        table_fields = json.loads(self.request.POST.get("fields"))
        table_options = json.loads(self.request.POST.get("table_options"))
        user = self.request.user
        new_schema = create_schema_model(user, table_fields, table_options)

        return HttpResponse(f'{new_schema.title}')


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
            'list_files': SchemaFileModel.objects.filter(data_schema_id=pk)
        }
        return self.render_to_response(context)

    # queryset = SchemaFieldsModel.objects.filter(key_schema_id=1)


def save_helper(schema_id, file):
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print(schema_id)
    to_update = SchemaFileModel.objects.get(id=schema_id)
    to_update.csv_file = file
    to_update.is_generated = True
    to_update.save()
    print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")


async def generate_data_helper(rows, schema, schema_fields_id, options=None, *args, **kwargs):
    sync_file = sync_to_async(create_csv_file)
    buffer = await sync_file(schema_id=schema_fields_id, rows_count=rows)
    file_db = ContentFile(buffer, name="temp.csv")
    save_schema = sync_to_async(save_helper)
    res = await save_schema(schema.id, file_db)
    await asyncio.sleep(1)


async def async_view(request, *args, **kwargs):
    # rows = int(request.POST.get("count_of_rows"))
    # schema_fields_id = kwargs.get("pk")
    # create_db_record = database_sync_to_async(SchemaFileModel.objects.create)
    # schema_model = await create_db_record(data_schema_id=schema_fields_id)
    # loop = asyncio.get_event_loop()
    # loop.create_task(generate_data_helper(rows, schema_model, schema_fields_id, *args, **kwargs))

    channel_layer = get_channel_layer()
    channel_layer.group_send(
        "file_creation",
        {"type": "message",  # Custom type
         "text": "Hello from HTTP view", }
    )
    # print(channel_layer)
    # channel_layer.send({
    #     "type": "send_file_message",
    #     "text": "Hello there!",
    # })

    return HttpResponse("Data is being generated...Please wait")
