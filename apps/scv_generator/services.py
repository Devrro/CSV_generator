import os
from uuid import uuid1

from django.contrib.auth import get_user_model

UserModel = get_user_model()


def upload_to(instance, file: str):
    user = UserModel.objects.get(dataschema__id=instance.data_schema_id)
    ext = file.split(",")[:-1]
    return os.path.join('users', f'user_id_{user.id}', f'{instance.data_schema_id}', "shemas", f"{uuid1()}.csv")
