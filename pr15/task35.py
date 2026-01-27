"""
Порахувати кількість від’ємних чисел
"""

def count_negative(nums):
    count = 0
    for n in nums:
        if n < 0:
            count += 1
    return count
