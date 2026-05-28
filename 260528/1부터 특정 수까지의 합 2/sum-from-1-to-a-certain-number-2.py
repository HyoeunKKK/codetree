N = int(input())

# Please write your code here.

def num(n):
    if n == 0:
        return 0
    return num(n-1)+n

print(num(N))