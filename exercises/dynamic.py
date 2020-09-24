# Validate the input only for the given fields, validate everything if fields param is None


# Rules for Person
# Name fields (first_name, middle_name, last_name)
#   Make sure each letter is alphabetical, with some special character allowance (O'Neill, Day-Lewis)
#   Ensure single spaces between words (some names may have spaces, e.g. 'van der Bellen')
#   Normalize to all caps
#   Trim whitespace
# middle_name -> optional
# date_of_birth -> ISO date (YYYY-MM-DD) parsed into datetime.date
# is_active -> Choices from ['T', 'F'], T' -> True, 'F' -> False


# Implement a validator function that accepts input data and a list of fields (or None)
# and dynamically validates the given fields (or all fields if fields=None) and returns cleaned & validated data


import datetime

from .util import compare


def my_validator(data, fields=None):
    # code goes here
    pass


INPUT_1 = {
    'first_name': 'Robert ',
    'last_name': '  Smith',
    'middle_name': 12345,
}

FIELDS_1 = ['first_name', 'last_name']

EXPECTED_1 = {
    'first_name': 'ROBERT',
    'last_name': 'SMITH'
}


INPUT_2 = {
    'first_name': 'barbara',
    'middle_name': None,
    'last_name': 'Vasquez',
    'date_of_birth': '1970-05-13',
    'is_active': 'F'
}

FIELDS_2 = None

EXPECTED_2 = {
    'first_name': 'BARBARA',
    'middle_name': None,
    'last_name': 'VASQUEZ',
    'date_of_birth': datetime.date(1970, 5, 13),
    'is_active': False
}


INPUT_3 = {
    'first_name': object(),
    'last_name': 'Brown',
    'date_of_birth': '1983-07-25',
    'is_active': 'T'
}

FIELDS_3 = ['last_name', 'date_of_birth', 'is_active']

EXPECTED_3 = {
    'last_name': 'BROWN',
    'date_of_birth': datetime.date(1983, 7, 25),
    'is_active': True
}


def check_validator(validator=my_validator):
    print('Validating INPUT_1, fields: {}'.format(FIELDS_1))

    compare(
        expected=EXPECTED_1,
        actual=validator(data=INPUT_1, fields=FIELDS_1))

    print('Validating INPUT_2, fields: {}'.format(FIELDS_2))

    compare(
        expected=EXPECTED_2,
        actual=validator(data=INPUT_2, fields=FIELDS_2))

    print('Validating INPUT_3, fields: {}'.format(FIELDS_3))

    compare(
        expected=EXPECTED_3,
        actual=validator(data=INPUT_3, fields=FIELDS_3))
