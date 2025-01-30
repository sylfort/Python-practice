input_line = input()

hmap = {
    "A":4,
    "E":3,
    "G":6,
    "I":1,
    "O":0,
    "S":5,
    "Z":2
}

final = ""

for char in input_line:
    if char.upper() in hmap:
        final += str(hmap[char])
    else:
        final += char
        
print(final)
