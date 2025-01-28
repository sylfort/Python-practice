import random

import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
    final()

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
        # guess = input("数字を入力すると、ヒット数と打撃数を教えてくれる")
        guess = str(editbox1.get())
        print(guess)
        if(len(guess) != 4):
            tmsg.showerror("エラー", "桁の数字を入力してください")
            print(("4桁の数字を入力してください"))
            break
        else:
            kazuok = True
            for i in range(4):
                if (guess[i] < "0" ) or (guess[i] > "9"):
                    tmsg.showerror("エラー", "数字ではありません")
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
            print(num_after_hit)
            print(guess_after_hit)
    return hit, num_after_hit, guess_after_hit

def blow_checker(a, b):
    total = 0
    for i in range(len(a)):
        current = a[i]
        # Create a version of b excluding the element at index i
        filtered_b = b[:i] + b[i+1:]
        total += filtered_b.count(current)
    return total

# def blow_checker(num, guess):
#     blow = 0
#
#     for i in guess:
#         print(num.count(i))
#         if num.count(i) == 1:
#             blow = blow + 1
#         elif num.count(i) == 2:
#             blow = blow + 2
#         elif num.count(i) == 3:
#             blow = blow + 3
#         elif num.count(i) == 4:
#             blow = blow + 3
#
#     return blow

def final():
    guess = isok()
    d = hit_checker(num, guess)
    
    hit = d[0]
    num_after_hit = d[1]
    guess_after_hit = d[2]
    
    blow = blow_checker(num_after_hit, guess_after_hit)
    
    print("ヒット: " + str(hit))
    print("ブロー: " + str(blow))

    if int(hit) < 4:
        tmsg.showinfo("test", "ヒット: " + str(hit) + "\nブロー: " + str(blow) + "\nもう一回当ててください")
    
    if int(hit) == 4:  
        tmsg.showinfo("当たり","おめでとうございます。当たりです")
        root.destroy()
    
num = n_digit_random_num(4)

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

label1 = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font =("Helvetica", 28))
editbox1.place(x= 120, y = 60)

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
button1.place(x = 220, y = 60)

root.mainloop()



