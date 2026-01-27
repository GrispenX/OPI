"""
Знайти суму парних чисел у списку
"""

def sum_even(nums):
    s = 0
    for n in nums:
        if n % 2 == 0:
            s += n
    return s
