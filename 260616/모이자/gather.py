n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min = 1000000
for i in range(n):
    target = A[i]
    A[i] = 0
    total = 0
    for j in range(n):
        total += A[j] * abs(i-j)
    if total < min:
        min = total
    A[i] = target

print(min)