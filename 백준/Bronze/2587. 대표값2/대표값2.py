num = list()
for _ in range(5):
    n = int(input())
    num.append(n)
num.sort()
a = int(sum(num)/5)
b = num[2]
print(a)
print(b)