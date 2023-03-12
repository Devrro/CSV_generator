# Generated by Django 4.1.7 on 2023-03-10 12:27

from django.db import migrations, models

import apps.scv_generator.services


class Migration(migrations.Migration):

    dependencies = [
        ('scv_generator', '0004_alter_fieldssavedoptionsmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemafilemodel',
            name='csv_file',
            field=models.FileField(blank=True, upload_to=apps.scv_generator.services.upload_to),
        ),
    ]
