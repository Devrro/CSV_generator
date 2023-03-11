import random
import uuid

from lorem.text import TextLorem

from apps.scv_generator.constants.list_data_companies import COMPANIES_NAME
from apps.scv_generator.constants.list_data_jobs import JOB_TITLES
from apps.scv_generator.constants.list_data_mails import MAILS_ENDINGS
from apps.scv_generator.constants.list_data_names import FEMAILE_NAMES, LAST_NAMES, MALE_NAMES


def get_full_name(gender: str = None) -> str:
    """
    Get string with full name
    :param gender: Leave empty for random gender. Write 'male' of 'female' to get corresponding full names
    :return: Returns formatted full name
    """

    full_name = []
    if gender is None:
        name_list = random.choice([FEMAILE_NAMES, MALE_NAMES])
        full_name.append(random.choice(name_list))
    if gender == "female":
        full_name.append(random.choice(FEMAILE_NAMES))
    if gender == "male":
        full_name.append(random.choice(MALE_NAMES))
    full_name.append(random.choice(LAST_NAMES))
    return " ".join(full_name)


def get_job_title() -> str:
    """
    Get job title
    :return:
    """
    return random.choice(JOB_TITLES)


def get_company(custom_list: list = None) -> str:
    """Returns random company name or from provided list"""
    if custom_list:
        return random.choice(custom_list)
    return random.choice(COMPANIES_NAME)


def get_email(
        full_name: str = None,
        start: str = None,
        ending: str = None,
        mail_addresses: str = None,
) -> str:
    """
    Get simple email address
    :param full_name:
    :param mail_addresses: You can provide list of your email addresses.
    :param start: Start of email address
    :param ending: Endings of string before "@" symbol
    :return:
    """
    if not full_name:
        full_name = "".join(str(uuid.uuid1()).split("-"))
    address = [] if start is None else [start]
    address.append(".".join(full_name.lower().split(" ")))
    if ending:
        address.append(ending)
    address.append("@")
    if not mail_addresses:
        address.append(random.choice(MAILS_ENDINGS))
    else:
        address.append(random.choice(mail_addresses))
    return "".join(address)


def get_phone_number(country_code: str = "38", operator_code: str = "098", number_of_digits_after: int = 7):
    last_digits = [str(random.randint(0, 9)) for _ in range(number_of_digits_after)]
    return f"+{country_code}{operator_code}{''.join(last_digits)}"


def get_text(words_count: int = 30) -> str:
    """
    Get lorem text
    :param words_count: Length of sentence
    :return:
    """
    return TextLorem(srange=(words_count, words_count)).sentence()


def get_integer(number_of_digits: int = 5) -> str:
    """
    Return number of needed length
    :param number_of_digits:
    :return:
    """
    return "".join([str(random.randint(0, 9)) for _ in range(number_of_digits)])


generator_dict = {
    "name": get_full_name,
    "job": get_job_title,
    "company": get_company,
    "mail": get_email,
    "phone_number": get_phone_number,
    "text": get_text,
    "integer": get_integer,
}
