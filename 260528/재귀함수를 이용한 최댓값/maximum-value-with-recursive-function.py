n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max_num(max_n,idx):
    if idx == n:
        return max_n
    if max_n < arr[idx]:
        max_n = arr[idx]
        idx += 1
        return max_num(max_n,idx)
    else:
        idx += 1
        return max_num(max_n,idx)


max_n = 1
idx = 0
print(max_num(max_n,idx))