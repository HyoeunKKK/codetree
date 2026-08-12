n,m,T,k = map(int,input().split())
marbles = []
mapper = {'L':0,'U':1,'D':2,'R':3}
for i in range(m):
    r,c,d,v = input().split()
    r,c,v = int(r)-1,int(c)-1,int(v)
    marbles.append([r,c,mapper[d],v,i+1])

grid = [[0 for _ in range(n)] for _ in range(n)]
for marble in marbles:
    grid[marble[0]][marble[1]] += 1

def in_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False

def move(marble):
    dr = [0,-1,1,0]
    dc = [-1,0,0,1]
    r = marble[0]
    c = marble[1]
    d = marble[2]
    V = marble[3]
    for v in range(V):
        if in_range(r+dr[d],c+dc[d]) == False:
            d = 3 - d
        r += dr[d]
        c += dc[d]
    return r,c,d,v
            

def move_all(marbles):
    count = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(marbles)):
        r,c,d,v = move(marbles[i])
        count[r][c] += 1
        marbles[i][0] = r
        marbles[i][1] = c
        marbles[i][2] = d
    return count,marbles


def duplicate_remove(marbles,count):
    temp_marbles = []
    for i in range(n):
        for j in range(n):
            if count[i][j] > k:
                remove_list = []
                for marble in marbles:
                    if marble[0] == i and marble[1] == j:
                        remove_list.append(marble)
                remove_list.sort(key=lambda x:(-x[3],-x[4]))
                temp_marbles.extend(remove_list[:k])
            elif 0 < count[i][j] <= k:
                extend_list = []
                for marble in marbles:
                    if marble[0] == i and marble[1] == j:
                        extend_list.append(marble)
                temp_marbles.extend(extend_list)
            else:
                pass
    return temp_marbles


for t in range(T):
    count,marbles = move_all(marbles)
    # print(marbles)
    marbles = duplicate_remove(marbles,count)
    # print(count)
    # print(marbles)

print(len(marbles))