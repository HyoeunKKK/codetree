n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(a,b):
    if 0 <= a < n and 0 <= b < n:
        return True
    else:
        return False

def not_loss(x,y,k):
    # coin = 0
    gold = 0
    cur_x = x
    cur_y = y-k
    for i in range(k+1):
        calc = 2*i+1
        for j in range(calc):
            if in_range(cur_x+j,cur_y) == True:
                # coin += 1
                if grid[cur_x+j][cur_y] == 1:
                    gold += 1
        cur_x -= 1
        cur_y += 1
    cur_x = x
    cur_y = y+k
    for i in range(k):
        calc = 2*i+1
        for j in range(calc):
            if in_range(cur_x+j,cur_y) == True:
                # coin += 1
                if grid[cur_x+j][cur_y] == 1:
                    gold += 1
        cur_x -= 1
        cur_y -= 1
    
    if gold*m >= (k**2+(k+1)**2):
        return True, gold
    else:
        return False, 0

real_num = 0
for i in range(n):
    for j in range(n):
        for k in range(n+1):
            a,b = not_loss(i,j,k)
            # print(a,b)
            if a == True:
                # print(i,j,k)
                if b > real_num:
                    real_num = b

print(real_num)
