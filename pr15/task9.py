"""
Знайти мінімальне число в списку
"""

def min_number(nums):
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    return m

print(min_number([5, 9, 3, 7, 2, 8]))