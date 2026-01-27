"""
Замінити всі пробіли на _
"""

def replace_spaces(text):
    result = ""
    for ch in text:
        if ch == " ":
            result += "_"
        else:
            result += ch
    return result
