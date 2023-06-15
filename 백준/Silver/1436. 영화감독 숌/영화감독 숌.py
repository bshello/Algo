N = int(input())

MM = 6660000
tmp = 0
for i in range(665, MM):
    j = str(i)
    if j.__contains__("666"):
        tmp += 1
    if tmp == N:
        print(int(j))
        break