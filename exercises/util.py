

def compare(expected, actual, path=''):
    """Recursive comparator to help with debugging"""
    assert type(expected) == type(actual), 'Different types, path: {}'.format(path)

    if isinstance(actual, dict):
        missing = set(expected.keys()).difference(actual.keys())
        extra = set(actual.keys()).difference(expected.keys())

        if extra:
            raise AssertionError('Extra keys in data: {}, path: {}'.format(extra, path))

        if missing:
            raise AssertionError('Missing keys from data: {}, path: {}'.format(missing, path))

        for key, value in expected.items():
            compare(value, actual[key], path='{} -> {}'.format(path, key))

    elif isinstance(actual, (list, tuple)):
        len_actual = len(actual)
        len_expected = len(expected)

        if len_actual != len_expected:
            raise AssertionError('Different sequence lengths (expected: {} vs actual: {}), Path: {}'.format(len_expected, len_actual), format(path))

        for idx, (v_expected, v_actual) in enumerate(zip(expected, actual)):
            compare(v_expected, v_actual, path='{} -> {}'.format(path, idx))

    else:
        if expected != actual:
            raise AssertionError('Expected: {} != Actual: {}, Path: {}'.format(expected, actual, path))