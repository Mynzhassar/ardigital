from . import constants


def validate_full_name(full_name):
    _validate_full_name_len(full_name)
    _validate_full_name_content(full_name)


def validate_telephone_number(telephone_number):
    telephone_number = telephone_number.replace('+', '')

    valid_len = _validate_tel_num_len(telephone_number)
    valid_operator = _validate_operator(telephone_number)
    valid_content = _validate_phone_num_content(telephone_number)

    if not valid_len or not valid_operator or not valid_content:
        raise ValueError('Некорректный номер телефона')


def validate_email(email):
    if '@' not in email or ' ' in email:
        raise ValueError('Некорректный email')

    _, mail = email.split('@')
    if '.' not in mail:
        raise ValueError('Некорректный email')


def _validate_full_name_len(full_name):
    if len(full_name.split()) != constants.VALID_FULL_NAME_LEN:
        raise ValueError('Пожалуйста, введите ваше имя и фамилию')


def _validate_full_name_content(full_name):
    for char in full_name.split():
        if not char.isalpha():
            raise ValueError(f'Некорректный символ {char}')


def _validate_tel_num_len(telephone_number):
    return len(telephone_number) == constants.VALID_PHONE_NUM_LEN


def _validate_operator(telephone_number):
    return telephone_number[1:4] in constants.VALID_PHONE_OPERATORS


def _validate_phone_num_content(telephone_number):
    for char in telephone_number:
        if not char.isdigit():
            return False

    return True
