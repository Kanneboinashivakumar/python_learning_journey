class InvalidAmountError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

class InvalidAccountError(Exception):
    pass

def validate_account(account_number):
    if account_number <= 0:
        raise InvalidAccountError("Account number must be positive.")

def validate_phone(phone):
    if len(phone) != 10 or not phone.isdigit():
        raise InvalidPhoneError("Phone number must contain exactly 10 digits.")

def validate_amount(amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")