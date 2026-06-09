N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

class_a = [0 for _ in range(N)]

for s in student:
    class_a[s-1] += 1
    if class_a[s-1] == K:
        print(s)
        break

if max(class_a) < K:
    print(-1)