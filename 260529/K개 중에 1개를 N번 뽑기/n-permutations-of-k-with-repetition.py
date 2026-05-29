K, N = map(int, input().split())

# Please write your code here.
item = []

def print_item():
    for i in item:
        print(i, end=' ')
    print()

def program(num):
    if num == N+1:
        print_item()
        return

    for i in range(1,K+1):
        item.append(i)
        program(num+1)
        item.pop()
    
program(1)
