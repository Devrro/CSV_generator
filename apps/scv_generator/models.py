from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

from apps.scv_generator.services import upload_to

UserModel = get_user_model()


# Create your models here.

class SchemaConfigsModel(models.Model):
    COMMA_SEP = "1"
    SEMICOLON_SEP = "2"
    QUOTE = "1"
    DOUBLE_QUOTE = "2"
    SEPARATOR_CHOICES = [
        (COMMA_SEP, "Comma (,)"),
        (SEMICOLON_SEP, "Semicolon (;)"),
    ]
    STRING_CHARACTER_CHOICES = [
        (QUOTE, "Quote (')"),
        (DOUBLE_QUOTE, 'Double-quote (")')
    ]
    data_schema = models.ForeignKey("DataSchema", on_delete=models.CASCADE)
    separator = models.CharField(choices=SEPARATOR_CHOICES, max_length=2)
    string_character = models.CharField(choices=STRING_CHARACTER_CHOICES, max_length=2)

    class Meta:
        db_table = "configs_of_tables"


class FieldDataTypesModel(models.Model):
    data_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'data_types'


class FieldsSavedOptionsModel(models.Model):
    key_field_schema = models.ForeignKey("SchemaFieldsModel", on_delete=models.CASCADE)
    options = models.JSONField(blank=True)


class SchemaFieldsModel(models.Model):
    key_schema = models.ForeignKey("DataSchema", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    data_field_name = models.CharField(max_length=255)
    data_type = models.ForeignKey("FieldDataTypesModel", on_delete=models.CASCADE)

    class Meta:
        db_table = "schema_fields"
        constraints = [
            UniqueConstraint(
                fields=["key_schema", "order"],
                name="Integer ordering for each new schema"
            )
        ]


class SchemaFileModel(models.Model):
    data_schema = models.ForeignKey("DataSchema", on_delete=models.CASCADE)
    is_generated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to=upload_to,blank=True)

    class Meta:
        db_table = "file_model_schema"


class DataSchema(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
