VALID_FULL_NAME_LEN = 2

VALID_PHONE_NUM_LEN = 11

VALID_PHONE_OPERATORS = {'700', '701', '702', '703', '704', '705', '706', '707', '708', '709',
                         '747', '750', '751', '760', '761', '762', '763', '764', '771', '775',
                         '776', '777', '778', }

CONSULTATION_STATUS_CHOICES = (
    ('NEW', 'NEW'),
    ('PROCESSED', 'PROCESSED'),
)

APPLICATION_STATUS_CHOICES = (
    ('NEW', 'NEW'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('CANCELED', 'CANCELED'),
    ('COMPLETED', 'COMPLETED'),
)

STATUS_NEW = 'NEW'

ARDIGITAL_EMAIL = '***'  # TODO

CONSULTATION_EMAIL_CONTENT = {
    'subject': 'Ваша заявка успешно сформирована!',
    'message': 'Ваша заявка на консультацию успешно сформирована! '
               'С Вами свяжутся в ближайшее время.',
}

APPLICATION_EMAIL_CONTENT = {
    'subject': 'Ваша заявка успешно сформирована!',
    'message': 'Ваша заявка успешно сформирована! С Вами свяжутся в ближайшее время.',
}
