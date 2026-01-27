"""
Знайти найбільше парне число
"""

import task8

def max_even(nums):
    evens = [n for n in nums if n % 2 == 0]
    return task8.max_number(evens)
