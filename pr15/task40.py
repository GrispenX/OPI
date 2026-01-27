"""
Обчислення степеня числа за допомогою циклу
"""

def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result
