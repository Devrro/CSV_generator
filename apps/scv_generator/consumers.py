# myapp/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer


class FileProcessingConsumer(AsyncWebsocketConsumer):

    def __init__(self):
        super(FileProcessingConsumer, self).__init__()

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=text_data)
