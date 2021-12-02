def calc(sign, a, b):
    try:
        if sign == '+':
            return a + b
        if sign == '-':
            return a - b
        if sign == '*':
            return a * b
        if sign == '/':
            if b != 0:
                return a / b
    except Exception:
        return None
