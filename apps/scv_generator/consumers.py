# myapp/consumers.py
import json
from asgiref.sync import sync_to_async, async_to_sync

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class FileProcessingConsumer(AsyncWebsocketConsumer):

    def __init__(self):
        super(FileProcessingConsumer, self).__init__()
        self.room_name = None
        self.websocket_id = None

    async def connect(self):
        await self.channel_layer.group_add(
            "file_creation",  # Group name
            self.channel_name,
        )
        await self.accept()
        self.room_name = "test"
        self.websocket_id = self.channel_name

    async def disconnect(self, close_code):
        await self.send(text_data=close_code)

    async def receive(self, text_data):
        await self.send(text_data=text_data)

    async def my_message(self, event):
        await self.send(text_data=event["text"])
    async def send_file_message(self, message):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message
        }))
