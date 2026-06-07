n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

lines = [0 for _ in range(200)]

for a,b in segments:
    ai = a+100
    bi = b+100
    for i in range(b-a):
        lines[ai+i] += 1

print(max(lines))