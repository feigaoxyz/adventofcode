"""
Common functions
"""


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, 'r') as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")


def validation(fn, input, expected):
    """Validate function on input versus expected result."""
    output = fn(*input)
    if output == expected:
        return True
    else:
        print('For input: {}; Output "{}" != Expected "{}"'.format(
            input, output, expected))
        raise AssertionError


def neighbors(loc, direction=8):
    """Return the neighbors of location,
    with direction being either 4 or 8.
    """
    assert direction in {4, 8}
    x, y = loc
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)
    if direction == 8:
        yield (x + 1, y + 1)
        yield (x + 1, y - 1)
        yield (x - 1, y + 1)
        yield (x - 1, y - 1)
