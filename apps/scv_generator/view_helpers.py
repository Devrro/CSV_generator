from asyncio import get_event_loop

from asgiref.sync import sync_to_async

from django.core.files.base import ContentFile

from apps.scv_generator.models import SchemaFileModel
from apps.scv_generator.services_generator import create_csv_file


def save_helper(schema_id, file):
    to_update = SchemaFileModel.objects.get(id=schema_id)
    to_update.csv_file = file
    to_update.is_generated = True
    to_update.save()


async def generate_data_helper(rows, schema, schema_fields_id, *args, **kwargs):
    loop = get_event_loop()
    buffer = await loop.run_in_executor(None, create_csv_file, schema_fields_id, rows)
    # sync_file = sync_to_async(create_csv_file)
    # buffer = await sync_file(schema_id=schema_fields_id, rows_count=rows)
    file_db = ContentFile(buffer, name="temp.csv")
    save_schema = sync_to_async(save_helper)
    res = await save_schema(schema.id, file_db)
