num = list()
for tc in range(9):
    n = int(input())
    num.append(n)
temp = 0
idx = 0
for i in range(len(num)):
    if temp < num[i]:
        temp = num[i]
        idx = i

print(temp)
print(idx+1)
