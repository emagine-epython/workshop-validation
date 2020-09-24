# Nested validation for same schema

# Rules for Person
# Name fields (first_name, middle_name, last_name)
#   Make sure each letter is alphabetical, with some special character allowance (O'Neill, Day-Lewis)
#   Ensure single spaces between words (some names may have spaces, e.g. 'van der Bellen')
#   Normalize to all caps
#   Trim whitespace
# middle_name -> optional
# date_of_birth -> ISO date (YYYY-MM-DD) parsed into datetime.date
# is_active -> Choices from ['T', 'F'], T' -> True, 'F' -> False
# friends -> List of Persons, can be empty, empty list if missing key

# You can use util module to compare your validated & cleaned result against the expected value:
# util.compare(expected=recursive.EXPECTED, actual=my_result)


import datetime


INPUT = {
    'first_name': 'Bob',
    'middle_name': None,
    'last_name': 'Smith',
    'date_of_birth': '1975-02-13',
    'is_active': 'T',
    'friends': [
        {
            'first_name': 'Jonathan',
            'last_name': '  Livingston  ',
            'date_of_birth': '1970-06-25',
            'is_active': 'F',
            'friends': [
                {
                    'first_name': 'Markus',
                    'last_name': 'Van   der Bellen',
                    'date_of_birth': '1968-12-25',
                    'is_active': 'T',
                },
                {
                    'first_name': 'Peter  ',
                    'middle_name': ' Richard',
                    'last_name': '  Day-Lewis ',
                    'date_of_birth': '1954-02-14',
                    'is_active': 'F',
                    'friends': []
                },                
            ]
        },
        {
            'first_name': 'Robert',
            'middle_name': 'Alexander',
            'last_name': 'McKinsey',
            'date_of_birth': '1986-04-30',
            'is_active': 'F',
        },
    ]
}


EXPECTED = {
    'first_name': 'BOB',
    'middle_name': None,
    'last_name': 'SMITH',
    'date_of_birth': datetime.date(1975, 2, 13),
    'is_active': True,
    'friends': [
        {
            'first_name': 'JONATHAN',
            'middle_name': None,
            'last_name': 'LIVINGSTON',
            'date_of_birth': datetime.date(1970, 6, 25),
            'is_active': False,
            'friends': [
                {
                    'first_name': 'MARKUS',
                    'middle_name': None,
                    'last_name': 'VAN DER BELLEN',
                    'date_of_birth': datetime.date(1968, 12, 25),
                    'is_active': True,
                    'friends': [],
                },
                {
                    'first_name': 'PETER',
                    'middle_name': 'RICHARD',
                    'last_name': 'DAY-LEWIS',
                    'date_of_birth': datetime.date(1954, 2, 14),
                    'is_active': False,
                    'friends': []
                },                
            ]
        },
        {
            'first_name': 'ROBERT',
            'middle_name': 'ALEXANDER',
            'last_name': 'MCKINSEY',
            'date_of_birth': datetime.date(1986, 4, 30),
            'is_active': False,
            'friends': []
        },
    ]
}