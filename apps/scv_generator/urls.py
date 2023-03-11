from django.urls import path

from apps.scv_generator.views import CreateSchemaView, ListUserSchemas, SchemaDetailView, async_view

urlpatterns = [
    path('', ListUserSchemas.as_view(), name="list_user_schemas"),
    path('/create_schema', CreateSchemaView.as_view(), name="create_schema"),
    path('/schema/<int:pk>', SchemaDetailView.as_view(), name="schema_details"),
    path('/schema/<int:pk>/generate_data', async_view, name="generate_data"),
    # path('create_schema_fields', ListUserSchemas.as_view(), name="list_user_schemas"),
]
