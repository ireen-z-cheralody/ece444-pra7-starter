def add(a, b):
    return a + b


def record(value, history=None):
    history.append(value)
    return history


# using E722: bare except
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
