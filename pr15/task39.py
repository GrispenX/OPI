"""
Знайти найдовше слово
"""

def longest_word(text):
    words = text.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
