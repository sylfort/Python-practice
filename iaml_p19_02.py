'''
Starting with 25, generate each term by taking half of the
previous term if it’s even, or multiplying by 3 and adding 1 if
it’s odd. (This is an instance of a Collatz sequence.)

'''
def calc_first_n_terms(n):
    arr = [25]
    
    while len(arr) < n:
        if arr[-1] % 2 == 0:
            arr.append(int(arr[-1] / 2))
        else:
            arr.append(int(arr[-1] * 3 + 1))
    
    return arr


print(calc_first_n_terms(3), "25, 76, 38")
print(calc_first_n_terms(5), "25, 76, 38, 19, 58")

def calc_nth_term(n):
    if n == 1:
        return 25
    else:
        previous = calc_nth_term(n-1)
        if previous % 2 == 0:
            return int(previous / 2)
        else:
            return int(previous * 3 + 1)
        

print(calc_nth_term(3), "38")
print(calc_nth_term(5), "58")
