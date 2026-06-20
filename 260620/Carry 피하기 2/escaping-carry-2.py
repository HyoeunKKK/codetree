n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from itertools import combinations

def add_line(a,b,c):
    a_len = [int(i) for i in range(a)]
    b_len = [int(i) for i in range(b)]
    c_len = [int(i) for i in range(c)]
    max_len = max(len(a_len),len(b_len),len(c_len))
    for i in range(max_len):
        a_row = a % 10
        a = a // 10
        b_row = b % 10
        b = b // 10
        c_row = c % 10
        c = c // 10
        if a_row + b_row + c_row < 10:
            continue
        else:
            return False
            break
    return True

comb_list = combinations(arr,3)

box = []
for a,b,c in comb_list:
    if add_line(a,b,c) == True:
        box.append(a+b+c)

if len(box) == 0:
    print(-1)
else:
    print(max(box))
     
