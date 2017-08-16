def generate():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        third = first + second
        yield third
        first = second
        second = third