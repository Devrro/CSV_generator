from django.urls import path

from apps.scv_generator.views import ListMainPage
from django.views.generic import TemplateView
from apps.scv_generator.views import ListUserSchemas

urlpatterns = [
    path('', ListUserSchemas.as_view(), name="list_user_schemas")
]
