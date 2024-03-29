# myapp/consumers.py
import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class FileProcessingConsumer(AsyncWebsocketConsumer):

    def __init__(self):
        super(FileProcessingConsumer, self).__init__()
        self.room_name = None
        self.websocket_id = None

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            "file_processing",  # Group name
            self.channel_name,
        )
        self.room_name = "test"

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "file_processing",  # Group name
            self.channel_name,
        )
        await self.send(text_data=close_code)

    async def receive(self, text_data): # noqa
        await self.send(text_data=text_data)

    async def file_updates(self, event):
        await self.send(json.dumps(event))
