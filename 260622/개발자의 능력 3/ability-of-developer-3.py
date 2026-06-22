abilities = list(map(int, input().split()))

# Please write your code here.

def get_diff(a,b,c):
    sum1 = a+b+c
    sum2 = sum(abilities)-sum1
    return abs(sum2-sum1)

min_diff = 5000000
for i in range(len(abilities)):
    for j in range(i+1,len(abilities)):
        for h in range(j+1,len(abilities)):
            min_diff = min(min_diff,get_diff(abilities[i],abilities[j],abilities[h]))

print(min_diff)