N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

# N: 개발자 수, K: 감염자가 전염병 옮기는 수, P: 초기 감염자, T: T번에 걸쳐 악수
# 0은 음성 1은 양성

handshakes.sort(key = lambda x: x[0])

dev = [0 for _ in range(N)]
dev[P-1] = 1
affect = [0 for _ in range(N)]


for hand in handshakes:
    a = hand[1]-1
    b = hand[2]-1
    if dev[a] == 1:
        if dev[b] == 1:
            affect[a] += 1
            affect[b] += 1
        else:
            if affect[a] < K:
                dev[b] = 1
                affect[a] += 1
    else:
        if dev[b] == 1:
            if affect[b] < K:
                dev[a] = 1
                affect[b] += 1
        
for d in dev:
    print(d, end='')