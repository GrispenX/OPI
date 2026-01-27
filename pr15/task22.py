"""
Вивести всі прості числа до 50
"""

import task21

for i in range(2, 51):
    if task21.is_prime(i):
        print(i)
