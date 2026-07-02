n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

def possible(max_val):
    available = []
    for i,value in enumerate(arr):
        if value <= max_val:
            available.append(i)
    for j in range(len(available)-1):
        if abs(available[j]-available[j+1]) > k:
            return False
    return True

minval = 100
min_end = max(arr[0],arr[-1])
for i in range(max(arr),min_end-1,-1):
    if possible(i) == True:
        minval = min(minval,i)


print(minval)