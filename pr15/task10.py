"""
Порахувати суму елементів списку
"""

def sum_list(nums):
    s = 0
    for n in nums:
        s += n
    return s

print(sum_list([1, 2, 3, 4, 5]))