"""
Функція перевірки паліндрому
"""

import task17

def is_palindrome(text):
    return text == task17.reverse_string(text)
