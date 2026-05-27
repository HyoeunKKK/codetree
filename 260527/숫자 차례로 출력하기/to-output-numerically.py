n = int(input())

# Please write your code here.



def num(n,start):
    if start > n:
        print()
        return
    print(start, end=' ')
    num(n,start+1)
    print(start, end=' ')


start = 1
num(n,start)