ability = list(map(int, input().split()))

# Please write your code here.

def get_diff(a,b,c):
    min_diff = min(a,b,c)
    max_diff = max(a,b,c)
    return max_diff - min_diff

length = len(ability)
min_diff = 3000000


for i in range(length):
    for j in range(i+1,length):
        sum1 = ability[i]+ability[j]
        ab2 = ability[0:i]+ability[i+1:j]+ability[j+1:length]
        # print(ab2)
        for k in range(len(ab2)):
            for h in range(k+1,len(ab2)):
                sum2 = ab2[k]+ab2[h]
                sum3 = sum(ability)-sum1-sum2
                diff = get_diff(sum1,sum2,sum3)
                # print(sum1,sum2,sum3)
                min_diff = min(min_diff,diff)
                # print(min_diff)

print(min_diff)