T = int(input())
num = list()
for tc in range(T):
    n = int(input())
    num.append(n)
num.sort()
for i in num:
    print(i)