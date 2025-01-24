# coding: utf-8
word = input()
word_list = list(word)
final = []
# for char in word_list[:]:
#     left = char
#     right = char + 1
#     print(left, right)
#     word_list.append(word_list[char])
#     if(left == "-" and right == "-"):
#       word_list.remove(word_list[char])
# print(word_list)
final.append(word_list[0])
for left, right in zip(word_list, word_list[1:]):
    # print(left, right)
    final.append(right)
    # print(final)
    if(left == "-" and right == "-"):
        final.pop()
        # print("removed ")
        # print(final)
print("".join(final))
    
