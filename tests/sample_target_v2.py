def compute(x):
    a = x + 1
    b = a * 2

    if x > 0:
        c = b + 10
        return c
    else:
        c = b - 10
        return c

    return 0


def nested_branch(n):
    if n > 10:
        if n % 2 == 0:
            return "big even"
        else:
            return "big odd"
    else:
        return "small"


def mixed_constructs(k):
    total = 0

    for i in range(k):
        total += i

    try:
        if total > 50:
            total = total // 2
        else:
            total += 5
    except Exception:
        total = -1

    while total < 100:
        total += 10

    return total