n,t = map(int,input().split())
conv = [list(map(int,input().split())) for _ in range(2)]


for i in range(t):
    temp1 = conv[0][-1]
    temp2 = conv[1][-1]
    cur1 = conv[0][0]
    cur2 = conv[1][0]
    for j in range(n-1):
        c1 = conv[0][j+1]
        c2 = conv[1][j+1]
        conv[0][j+1] = cur1
        conv[1][j+1] = cur2
        cur1 = c1
        cur2 = c2
    conv[0][0] = temp2
    conv[1][0] = temp1

for C in conv:
    for c in C:
        print(c,end=' ')
    print()