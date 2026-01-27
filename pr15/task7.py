"""
Порахувати кількість символів у рядку
"""

def count_chars(text):
    count = 0
    for _ in text:
        count += 1
    return count

print(count_chars("Hello"))