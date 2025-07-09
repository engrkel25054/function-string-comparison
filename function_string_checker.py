# Program specification
"""
1. Write a function is_in that accepts two strings as arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in str operator in.

2. Write a function to test is_in.
"""

def is_in(s1, s2):
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    return False

def test_is_in(s1_tuple, s2_tuple):
    for s in str1:
        for st in str2:
            if is_in(s, st):
                print(f"The word,\"{s}\", is in both str1 and str2.")


str1 = ("winner", "loser", "together", "villain")
str2 = ("champion", "winner", "villain", "neutral")

print("str1 =", str1)
print("str2 =", str2)
print()
test_is_in(str1, str2)

