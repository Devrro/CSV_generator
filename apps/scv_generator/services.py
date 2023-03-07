import os
from io import BytesIO
from uuid import uuid1
from models import SchemaFieldsModel
from generators import generator_dict


def upload_to(instance, file: str):
    ext = file.split(",")[:-1]
    return os.path.join(instance.id, "shema", f"{uuid1()}.{ext}")


def create_csv_file(
        schema_id: int,
        rows_count: int,
        separator: str = ",",
        string_character: str = "\"",
        **kwargs,
):
    list_of_fields = SchemaFieldsModel.objects.filter(key_schema_id=1).order_by("order")
    list_of_fields = list(list_of_fields.values('data_type__data_type', 'data_field_name'))
    column_heads = [field["data_field_name"] for field in list_of_fields]
    column_operators = [field["data_type__data_type"] for field in list_of_fields]

    options = {
        "name": {"gender": kwargs.get("gender", None)},
        "company": {"custom_list": kwargs.get("custom_list", [])},
        "email": {
            "start": kwargs.get("start", None),
            "ending": kwargs.get("ending", None),
            "mail_addresses": kwargs.get("mail_addresses", [])},
        "phone_number": {
            "country_code": kwargs.get("country_code", "380"),
            "operator_code": kwargs.get("operator_code", "98"),
            "number_of_digits_after": kwargs.get("number_of_digits_after", 7),
        },
        "text": {
            "words_count": kwargs.get("words_count", 30)
        },
        "integer": {
            "number_of_digits": kwargs.get("number_of_digits", 7)
        }
    }
    buffer = BytesIO()
    with buffer as buf:
        buf.write(f"{separator}".join(column_heads))
        for row in range(rows_count):
            value = []
            for operator in column_operators:
                option_dict = options.get(operator, None)
                if option_dict:
                    value.append(generator_dict[operator](**option_dict))
                else:
                    value.append(generator_dict[operator]())
            value_str = f"{separator}".join(value)
            buf.write(value_str)

    return buffer
