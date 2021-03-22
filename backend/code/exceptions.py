class InvalidNameError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class InvalidTelephoneNumberError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class InvalidEmailAddressError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
