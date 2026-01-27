"""
Знайти середнє парних чисел
"""

def average_even(nums):
    evens = [n for n in nums if n % 2 == 0]
    return sum(evens) / len(evens)
