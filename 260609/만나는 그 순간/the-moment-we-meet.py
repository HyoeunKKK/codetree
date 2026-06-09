n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.

a_loc = 0
b_loc = 0

for i in range(1,len(t)):
    t[i] += t[i-1]

for i in range(1,len(t2)):
    t2[i] += t2[i-1]

def direction(dir,loc):
    if dir == 'R':
        loc += 1
        return loc
    else:
        loc -= 1
        return loc

def location(loc,now,t):      # loc: 1,2,3,4.. now: 0
    if loc <= t[now]:
        return now
    else:
        return now+1
        
t_time = t[-1]
t_loc = 1
t_now = 0
t2_now = 0

for i in range(t_time):
    t_now = location(t_loc,t_now,t)
    t2_now = location(t_loc,t2_now,t2)
    a_loc = direction(d[t_now],a_loc)
    b_loc = direction(d2[t2_now],b_loc)
    # print(a_loc, b_loc)
    if a_loc == b_loc:
        print(t_loc)
        break
    else:
        t_loc += 1

if t_loc-1 == t_time:
    print(-1)
    
