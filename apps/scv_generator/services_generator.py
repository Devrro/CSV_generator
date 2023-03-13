import csv
import io

from apps.scv_generator.constants.scv_config import SEPARATOR_CHOICES, STRING_CHARACTER_CHOICES
from apps.scv_generator.generators import generator_dict
from apps.scv_generator.models import SchemaConfigsModel, SchemaFieldsModel

# def get_csv_fields_options(**kwargs) -> dict:
#     return {
#         "name": {"gender": kwargs.get("gender", None)},
#         "company": {"custom_list": kwargs.get("custom_list", [])},
#         "email": {
#             "start": kwargs.get("start", None),
#             "ending": kwargs.get("ending", None),
#             "mail_addresses": kwargs.get("mail_addresses", [])},
#         "phone_number": {
#             "country_code": kwargs.get("country_code", "380"),
#             "operator_code": kwargs.get("operator_code", "98"),
#             "number_of_digits_after": kwargs.get("number_of_digits_after", 7),
#         },
#         "text": {
#             "words_count": kwargs.get("words_count", 30)
#         },
#         "integer": {
#             "range_from": kwargs.get("range_from", 0),
#             "range_to": kwargs.get("range_to", 10000)
#         }
#     }


def create_csv_file(
        schema_id: int,
        rows_count: int = 100,
        **kwargs,
):
    list_of_fields = SchemaFieldsModel.objects.filter(key_schema_id=schema_id).order_by("order")
    list_of_fields = list(list_of_fields.values('data_type__data_type', 'data_field_name'))
    separator_id, string_char_id = list(
        SchemaConfigsModel.objects.filter(
            data_schema_id=schema_id
        ).values_list(
            "separator",
            "string_character"
        ))[0]

    separator_symbol = SEPARATOR_CHOICES[int(separator_id)-1][1]
    string_char_symbol = STRING_CHARACTER_CHOICES[int(separator_id)-1][1]

    column_heads = [field["data_field_name"] for field in list_of_fields]
    column_operators = [field["data_type__data_type"] for field in list_of_fields]
    # options = get_csv_fields_options(**kwargs)

    buffer = io.StringIO('', newline='')
    writer = csv.writer(
        buffer,
        delimiter=separator_symbol,
        quotechar=string_char_symbol,
        quoting=csv.QUOTE_MINIMAL,
        lineterminator='\n')

    writer.writerow(column_heads)
    for row in range(rows_count):
        value = []
        for operator in column_operators:
            # option_dict = options.get(operator, None)
            # if option_dict:
            #     value.append(generator_dict[operator](**option_dict))
            #     continue
            generated_value = generator_dict.get(operator, None)()
            value.append(generated_value)
        writer.writerow(value)
    return buffer.getvalue()
