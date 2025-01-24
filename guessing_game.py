import random

def n_digit_random_num(n):
        num = []
        for i in range(n): 
            a = str(random.randint(0,9))
            num.append(a)
        print(num)
        return num

def isok():
    isok = False        
    while isok == False:
        guess = input("数字を入力すると、ヒット数と打撃数を教えてくれる")
        if(len(guess) != 4):
            print(("4桁の数字を入力してください"))
        else:
            kazuok = True
            for i in range(4):
                if (guess[i] < "0" ) or (guess[i] > "9"):
                    print(("4桁の数字を入力してください"))
                    kazuok = False
                    break
            if kazuok :
                    isok = True   
    return guess

def hit_checker(num, guess):
    hit = 0
    num_after_hit = []
    guess_after_hit = []
    for n, g in zip(num, guess): 
        if n == g:
            hit += 1
        else:
            num_after_hit.append(n)
            guess_after_hit.append(g)
    return hit, num_after_hit, guess_after_hit

def blow_checker(num_after_hit, guess_after_hit):
    blow = 0

    for i in guess_after_hit:
        if num_after_hit.count(i) == 1:
            blow = 1
        elif num_after_hit.count(i) == 2:
            blow = 2
        elif num_after_hit.count(i) == 3:
            blow = 3

    return blow

def final():
    guess = isok()
    d = hit_checker(num, guess)
    
    hit = d[0]
    num_after_hit = d[1]
    guess_after_hit = d[2]
    
    blow = blow_checker(num_after_hit, guess_after_hit)
    
    print("ヒット: " + str(hit))
    print("ブロー: " + str(blow))

    while int(hit) < 4:
        final()
        
    print("おめでとう！")

num = n_digit_random_num(4)
final()
