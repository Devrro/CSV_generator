# myapp/routing.py
from django.urls import path

from apps.scv_generator.consumers import SomeConsumer

websocket_urlpatterns = [
    path('ws/file_ready/', SomeConsumer.as_asgi(), name='websocket'),
]
