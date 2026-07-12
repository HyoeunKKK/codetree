n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def grid_coin(x,y):
    coin = 0
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == 1:
                coin += 1
    return coin

result = 0
for i in range(n-2):
    for j in range(n-2):
        coin_total = grid_coin(i,j)
        if result < coin_total:
            result = coin_total

print(result)
