from validate_email import validate_email

from . import constants, exceptions


def validate_full_name(full_name):
    _validate_full_name_len(full_name)
    _validate_full_name_content(full_name)


def validate_telephone_number(telephone_number):
    telephone_number = telephone_number.replace('+', '')

    _validate_phone_num_content(telephone_number)
    _validate_tel_num_len(telephone_number)
    _validate_operator(telephone_number)


def validate_email_address(email):
    try:
        validation_result = validate_email(email)
    except Exception:
        raise exceptions.InvalidEmailAddressError('Некорректный email')

    if not validation_result:
        raise exceptions.InvalidEmailAddressError('Некорректный email')


def _validate_full_name_len(full_name):
    if len(full_name.split()) != constants.VALID_FULL_NAME_LEN:
        raise exceptions.InvalidNameError('Пожалуйста, введите ваше имя и фамилию')


def _validate_full_name_content(full_name):
    for char in ''.join(full_name.split()):
        if not char.isalpha():
            raise exceptions.InvalidNameError(f'Некорректный символ {char}')


def _validate_phone_num_content(telephone_number):
    for char in telephone_number:
        if not char.isdigit():
            raise exceptions.InvalidTelephoneNumberError(f'Некорректный символ {char}')


def _validate_tel_num_len(telephone_number):
    if len(telephone_number) != constants.VALID_PHONE_NUM_LEN:
        raise exceptions.InvalidTelephoneNumberError('Недостаточно символов')


def _validate_operator(telephone_number):
    if telephone_number[1:4] not in constants.VALID_PHONE_OPERATORS:
        raise exceptions.InvalidTelephoneNumberError('Некорректный оператор мобильной связи')
