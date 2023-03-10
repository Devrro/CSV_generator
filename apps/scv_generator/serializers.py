# Pseudo serializer file. Just needed to separate logic from view
from django.db.transaction import atomic

from apps.scv_generator.models import DataSchema, FieldsSavedOptionsModel, SchemaConfigsModel, SchemaFieldsModel


@atomic
def create_schema_model(user, fields: list[dict], table_options: dict):
    schema_object = DataSchema.objects.create(
        user=user,
        title=table_options.get("schema_name", "New schema")
    )

    SchemaConfigsModel.objects.create(
        data_schema=schema_object,
        separator=table_options.get("column_separator", "1"),
        string_character=table_options.get("string_character", "1")
    )

    schema_fields = []

    for field in fields:
        schema_field = SchemaFieldsModel.objects.create(
            key_schema=schema_object,
            order=int(field.get("order")),
            data_type_id=int(field.get("data_type")),
            data_field_name=field.get("column_name", "Field name"),
        )
        schema_fields.append(schema_field)

    # Save additional fields options as json objects in db
    # Not developed yet
    json_options = list(filter(lambda x: x.get("option_values" != ''), fields))
    schema_fields = list(
        filter(lambda x: x.order in list(map(lambda y: y.get("order"), json_options)), schema_fields))

    if json_options:
        for json_option in json_options:
            FieldsSavedOptionsModel.objects.create(
                key_field_schema=(
                    list(filter(lambda x: x.order == int(json_option.get("order")), schema_fields))[0],
                    schema_fields),
                options=json_option.get("oprion_values")
            )
    return schema_object
