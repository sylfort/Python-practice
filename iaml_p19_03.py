'''
Starting with 0, 1, generate each term by adding the previous
two terms. (This is the famous Fibonacci sequence.)

'''
def calc_first_n_terms(n):
    arr = [0, 1]
    
    while len(arr) < n:
        arr.append(arr[-1] + arr[-2])
    return arr

def calc_nth_term(n):
    if n == 1:
        return 0
    
    elif n == 2:
        return 1
    else:
        return calc_nth_term(n - 1) + calc_nth_term(n - 2)
    
    
print(calc_first_n_terms(3), "0, 1, 1")
print(calc_first_n_terms(6), "0, 1, 1, 2, 3, 5")

print(calc_nth_term(3), "1")
print(calc_nth_term(6), "5")
