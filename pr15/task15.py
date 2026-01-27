"""
Порахувати кількість парних чисел у списку
"""

def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count