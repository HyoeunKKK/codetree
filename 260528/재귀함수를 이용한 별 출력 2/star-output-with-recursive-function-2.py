n = int(input())

# Please write your code here.

def star(n):
    if n == 0:
        return
    print('* '*n)
    n -= 1
    star(n)
    print('* '*(n+1))


star(n)
