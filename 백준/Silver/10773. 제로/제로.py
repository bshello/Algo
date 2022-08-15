T = int(input())
num = list()
for i in range(T):
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        del num[-1]

print(sum(num))