commands = input()

# Please write your code here.

coms = list(commands)

x = 0
y = 0
num = 0
ans = -1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

curr = 0

for com in coms:
    if com == 'F':
        x += dx[curr]
        y += dy[curr]
    elif com == 'L':
        curr -= 1
        curr = curr % 4
    else:
        curr += 1
        curr = curr % 4
    num += 1
    if x == 0 and y == 0:
        ans = num
        break

print(ans)
    
