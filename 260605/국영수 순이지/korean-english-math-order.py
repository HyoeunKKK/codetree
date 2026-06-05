n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class Student:
    def __init__(self, name, gug, yeong, su):
        self.name = name
        self.gug = gug
        self.yeong = yeong
        self.su = su

students = []
for i in range(n):
    s = Student(name[i],korean[i],english[i],math[i])
    students.append(s)

students.sort(key=lambda x: (-x.gug, -x.yeong, -x.su))

for i in students:
    print(i.name, i.gug, i.yeong, i.su)