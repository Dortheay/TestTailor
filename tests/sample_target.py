def simple_function(x):
    a = x + 1
    b = a * 2
    c = b - 3
    return c


def conditional_function(x):
    if x > 10:
        y = x * 2
        z = y + 5
        return z
    else:
        y = x - 2
        return y


def loop_function(n):
    total = 0
    for i in range(n):
        total += i

    while total < 100:
        total += 10

    return total