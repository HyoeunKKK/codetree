n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

arr.append(-1)

cnt = 0
max_cnt = 1

for i in range(n):
    cnt += 1
    if arr[i] != arr[i+1]:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 0

print(max_cnt)
