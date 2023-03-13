import os
from uuid import uuid1

from channels.layers import get_channel_layer

from django.contrib.auth import get_user_model

UserModel = get_user_model()


def upload_to(instance, file: str):
    user = UserModel.objects.get(dataschema__id=instance.data_schema_id)
    return os.path.join('users', f'user_id_{user.id}', f'{instance.data_schema_id}', "tables", f"{uuid1()}.csv")


async def send_message_file_updates(channel_name, data: dict):
    channel_layer = get_channel_layer()
    await channel_layer.group_send(channel_name, data)
