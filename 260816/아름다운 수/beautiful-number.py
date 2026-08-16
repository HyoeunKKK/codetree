n = int(input())

# Please write your code here.

beautiful_num = 0

def find_beautiful(cur_len):
    global n,beautiful_num
    if cur_len == n:
        # print('beautiful')
        beautiful_num += 1
        return
    elif cur_len < n:
        for i in range(1,5):
            # print(cur_len,i)
            find_beautiful(cur_len+i)
    else:
        # print('over')
        return


find_beautiful(0)
print(beautiful_num)