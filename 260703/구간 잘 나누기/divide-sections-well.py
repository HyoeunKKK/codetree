n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

def possible(max_num):
    cur = 0
    cnt = 1
    for x in a:
        if cur+x <= max_num:
            cur += x
        else:
            cnt += 1
            cur = x

    return cnt <= m
    
            
min_total = max(a)
max_total = sum(a)
ans = max_total

while min_total <= max_total:
    mid = (min_total + max_total) // 2
    if possible(mid) == True:
        ans = mid
        max_total = mid - 1
    else:
        min_total = mid + 1

print(ans)