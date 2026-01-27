"""
Видалити всі нулі зі списку
"""

def remove_zeros(nums):
    result = []
    for n in nums:
        if n != 0:
            result.append(n)
    return result
