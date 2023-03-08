import json

from channels.generic.websocket import AsyncWebsocketConsumer
from apps.scv_generator.services import create_csv_file


class FileStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        result = await create_csv_file(text_data.get('schema_id'))

        await self.send(text_data=json.dumps({"result": result}))
