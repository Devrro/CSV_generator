# Generated by Django 4.1.7 on 2023-03-08 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scv_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldsSavedOptionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.JSONField()),
                ('key_field_schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scv_generator.schemafieldsmodel')),
            ],
        ),
    ]
