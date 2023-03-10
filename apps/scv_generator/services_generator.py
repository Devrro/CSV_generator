import io
from io import BytesIO, StringIO, FileIO

from apps.scv_generator.generators import generator_dict
from apps.scv_generator.models import SchemaFieldsModel
from django.core.files.base import ContentFile
import csv
import tempfile


def get_csv_options(**kwargs) -> dict:
    return {
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


def create_csv_file(
        schema_id: int,
        rows_count: int = 100,
        separator: str = ",",
        string_character: str = "\"",
        **kwargs,
):
    print("------------------------")
    rows_count = 10*2
    list_of_fields = SchemaFieldsModel.objects.filter(key_schema_id=schema_id).order_by("order")
    list_of_fields = list(list_of_fields.values('data_type__data_type', 'data_field_name'))
    column_heads = [field["data_field_name"] for field in list_of_fields]
    column_operators = [field["data_type__data_type"] for field in list_of_fields]
    print(column_heads)
    print(column_operators)
    options = get_csv_options(**kwargs)
    tmp_file_path: str = ''

    with tempfile.NamedTemporaryFile("w", delete=True) as tmp_file:
        tmp_file_path = tmp_file.name + ".csv"
        tmp_file.close()
        buffer = io.StringIO('', newline='')

        writer = csv.writer(buffer, delimiter=f",", quotechar="'", quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(column_heads)
        for row in range(rows_count):
            value = []
            for operator in column_operators:
                option_dict = options.get(operator, None)
                if option_dict:
                    value.append(generator_dict[operator](**option_dict))
                    continue
                generated_value = generator_dict.get(column_operators[0], None)()
                value.append(generated_value)
            if rows_count % 1000 == 0:
                print(value)
            writer.writerow(value)
        # csv_file.close()


# buffer = BytesIO()
# img.save(stream=buffer, format="CSV")
    return buffer.getvalue()
# with open(file, "r") as n_file:
#     buffer.writelines(n_file.readlines())
# return tmp_file_path
