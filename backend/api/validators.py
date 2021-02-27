from . import constants


def validate_full_name(full_name):
    _validate_full_name_len(full_name)
    _validate_full_name_content(full_name)


def validate_telephone_number(telephone_number):
    with_plus = telephone_number[0] == '+'

    valid_len = _validate_tel_num_len(telephone_number, with_plus)
    valid_operator = _validate_operator(telephone_number, with_plus)
    valid_content = _validate_phone_num_content(telephone_number, with_plus)

    if not valid_len or not valid_operator or not valid_content:
        raise ValueError('Некорректный номер телефона')


def _validate_full_name_len(full_name):
    if len(full_name.split()) != constants.VALID_FULL_NAME_LEN:
        raise ValueError('Пожалуйста, введите ваше имя и фамилию')


def _validate_full_name_content(full_name):
    for char in full_name:
        if not char.isalpha():
            raise ValueError(f'Некорректный символ {char}')


def _validate_tel_num_len(telephone_number, with_plus):
    tel_num_len = len(telephone_number)

    return tel_num_len == constants.VALID_PHONE_NUM_LEN or (
            tel_num_len == constants.VALID_PHONE_NUM_LEN_WITH_PLUS and with_plus)


def _validate_operator(telephone_number, with_plus):
    operator = telephone_number[2:5] if with_plus else telephone_number[1:4]
    return operator in constants.VALID_PHONE_OPERATORS


def _validate_phone_num_content(telephone_number, with_plus):
    for char in telephone_number:
        if not (char.isdigit() or (char == '+' and with_plus)):
            return False
