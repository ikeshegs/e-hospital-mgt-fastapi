from datetime import datetime


def convert_string_to_date(date_string: str):
    date_object = datetime.strptime(date_string, '%d/%m/%Y').date()
    return date_object


def convert_string_to_datetime(datetime_string: str):
    datetime_object = datetime.strptime(datetime_string, '%d/%m/%Y %H:%M:%S')
    return datetime_object
