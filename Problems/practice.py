
def luckyOrderID(token):
    if token == 0:
        return 0
    if token == 1 or token == 2:
        return 1

    a = b = 1

    for i in range(2, token):
        a, b = b, a + b
    return b
