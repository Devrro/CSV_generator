import os
from uuid import uuid1
from models import SchemaFieldsModel


def upload_to(instance, file: str):
    ext = file.split(",")[:-1]
    return os.path.join(instance.id, "shema", f"{uuid1()}.{ext}")


def create_csv_file(schema_id: int, rows_count: int):
    list_of_fields = SchemaFieldsModel.objects.filter(schema_id=schema_id).order_by("order")
    list_of_fields = list_of_fields.values("data_type__data_type",
                                           "data_field_name",
                                           "shema__schemafieldsmodel__order")
