import itertools

_counter = itertools.count(1)


def generate_id():
    return next(_counter)