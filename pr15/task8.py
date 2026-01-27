"""
Знайти максимальне число в списку
"""

def max_number(nums):
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m

print(max_number([3, 7, 2, 9]))
