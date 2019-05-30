import re


class Allow():

    def alphanumeric(self, data):
        # Allow letters, numbers and underspace
        if not re.match(r'(^[\w._]+$)', data, re.UNICODE):
            return False
        return data

    def letters(self, data):
        # Allow only letters
        if not re.match(r'(^[\D.]+$)', data, re.UNICODE):
            return False
        return data

    def numbers(self, data):
        # Allow only numbers
        if not re.match(r'(^[\d]+$)', data, re.UNICODE):
            return False
        return data

    def password_check(self, data):
        # Verify the strength of 'password'
        # Returns a dict with info
        # A password is considered strong when all true:
        #     8 characters length or more
        #     1 digit or more
        #     1 symbol or more
        #     1 uppercase letter or more
        #     1 lowercase letter or more

        # check the length
        length_error = len(data) < 8

        # check digits
        digit_error = re.search(r"\d", data) is None

        # check uppercase
        uppercase_error = re.search(r"[A-Z]", data) is None

        # check lowercase
        lowercase_error = re.search(r"[a-z]", data) is None

        # check symbols
        symbol_error = re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', data) is None

        # result
        password_ok = not (
            length_error or digit_error or uppercase_error or
            lowercase_error or symbol_error
        )
        if password_ok:
            return data
        return {
            # 'Password': data, # uncoment if password is need
            'ok': password_ok,
            'Length': length_error,
            'Digit': digit_error,
            'Uppercase': uppercase_error,
            'Lowercase': lowercase_error,
            'Symbol': symbol_error,
        }
