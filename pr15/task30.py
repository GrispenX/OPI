"""
Сума цифр числа
"""

def sum_digits(n):
    s = 0
    for d in str(abs(n)):
        s += int(d)
    return s
