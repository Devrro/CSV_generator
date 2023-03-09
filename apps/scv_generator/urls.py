from django.urls import path

from apps.scv_generator.views import ListMainPage, SchemaDetailView, CreateSchemaView
from django.views.generic import TemplateView
from apps.scv_generator.views import ListUserSchemas

urlpatterns = [
    path('', ListUserSchemas.as_view(), name="list_user_schemas"),
    path('create_schema', CreateSchemaView.as_view(), name="create_schema"),
    path('schema/<int:pk>', SchemaDetailView.as_view(), name="schema_details"),
    # path('create_schema_fields', ListUserSchemas.as_view(), name="list_user_schemas"),
]
