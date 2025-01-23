# coding: utf-8
input = input()
output = ""

def is_vowel(char):
    return char in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for a in input:
    if not (is_vowel(a)):
        output += a
print(output)
