n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def happynum(a,b):
    if a == 0:
        num = 1
        total_num = 1
        for i in range(n-1):
            start = grid[b][i]
            if start == grid[b][i+1]:
                num += 1
                if total_num < num:
                    total_num = num
            else:
                num = 1
                pass
    else:
        num = 1
        total_num = 1
        for i in range(n-1):
            start = grid[i][b]
            if start == grid[i+1][b]:
                num += 1
                if total_num < num:
                    total_num = num
            else:
                num = 1
                pass
    return total_num

result = 0

for i in range(2):
    for j in range(n):
        if happynum(i,j) >= m:
            result += 1

print(result)

