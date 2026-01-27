"""
Знайти індекс елемента у списку
"""

def find_index(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1
