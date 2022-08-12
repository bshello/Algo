school = int(input())
studentl = list()
applel = list()

for i in range(school):
    student, apple = map(int, input().split())
    studentl.append(student)
    applel.append(apple)

s = 0

for j in range(school):
    s += applel[j] % studentl[j]

print(s)
