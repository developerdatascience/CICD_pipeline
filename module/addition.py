def add_two_numbers(a: int, b: int) ->int:
    return a + b


def sum(*args) ->int:
    s=0
    for i in args:
        s = s + i
    return s
    