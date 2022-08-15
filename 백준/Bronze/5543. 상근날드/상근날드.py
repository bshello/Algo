burger=list()
bev = list()
for i in range(3):
    i = int(input())
    burger.append(i)
for j in range(2):
    j = int(input())
    bev.append(j)
burger.sort()
bev.sort()
ans = burger[0] + bev[0] - 50
print(ans)