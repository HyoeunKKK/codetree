secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class secret:
    def __init__(self,code,point,time):
        self.code = code
        self.point = point
        self.time = time

S = secret(secret_code,meeting_point,time)
print('secret code :', S.code)
print('meeting point :', S.point)
print('time :', S.time)