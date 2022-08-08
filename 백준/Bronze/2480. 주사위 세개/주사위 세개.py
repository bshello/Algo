dice = list(map(int, input().split()))
dc = list()
cnt = 0

for i in dice:
    if i in dc :
        cnt +=1
        dc.append(i)
    else:
        dc.append(i)

dc.sort()

if cnt == 2:
    money = 10000 + dc[0]*1000
elif cnt ==1:
    if dc[0] == dc[1]:
        money = 1000 + dc[0]*100
    else:
        money = 1000 + dc[1]*100
else:
    money = dc[2]*100

print(money)
