'''
write a function to generate an array containing first n terms,
and then write a separate recursive function to generate the nth term.
Be sure to work these sequences out by hand and write tests.
1. Starting with 5, generate each term by multiplying the previous
term by 3 and subtracting 4.
'''
def first_n_terms_array(n):
    arr = [5]
    
    while len(arr) < n:
        
        arr.append(arr[-1] * 3  - 4)
    return arr
    

print(first_n_terms_array(3), "5, 11, 29")
print(first_n_terms_array(5), "5, 11, 29, 83, 245")
