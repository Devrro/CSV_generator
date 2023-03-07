from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class FieldDataTypesModel(models.Model):
    data_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'data_types'


class SchemaFieldsModel(models.Model):
    schema = models.ForeignKey("SchemaModel", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    data_field_name = models.CharField(max_length=255)
    data_type = models.ForeignKey("FieldDataTypesModel", on_delete=models.CASCADE)

    class Meta:
        db_table = "schema_fields"
        constraints = [
            UniqueConstraint(
                fields=["schema", "order"],
                name="Integer ordering for each new schema"
            )
        ]


class SchemaModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    is_generated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    csv_file = models.FileField(blank=True)

    class Meta:
        db_table = "user_schemas"
