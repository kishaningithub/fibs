def generate():
    first = 0
    yield first
    second = 1
    yield first
    while True:
        third = first + second
        yield third
        first = second
        second = third