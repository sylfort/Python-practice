# Write a Python function called find_special_numbers that takes two integers, 
# start and end, and returns a list of numbers between start and end (inclusive) 
# that meet all of the following conditions:
#
# The number is divisible by both 3 and 5 (i.e., divisible by 15).
#
# The number is not divisible by 10.
#
# The function should work whether start is less than or greater than end.
#
# Examples:
#
# find_special_numbers(1, 30) → [15]

def find_special_numbers(start, end):
    numList = []
    for i in range(start, end + 1):
        if((i%3 == 0) and (i%5 == 0) and (i%10 != 0)):
            numList.append(i)
    
    return numList


c = find_special_numbers(1, 30)
print(c)
