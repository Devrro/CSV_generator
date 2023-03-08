# myapp/routing.py
from django.urls import path
from apps.scv_generator.consumers import SomeConsumer

websocket_urlpatterns = [
    path('ws/some-path/', SomeConsumer.as_asgi()),
]
