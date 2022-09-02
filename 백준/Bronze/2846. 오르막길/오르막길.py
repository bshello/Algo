n = int(input())
road = list(map(int, input().split()))
temp = []
ans = []
for i in range(1, n):
    if road[i] > road[i-1]:
        temp.append(road[i-1])
        if i == n-1:
            temp.append(road[i])
            temp.sort()
            ans.append(temp[-1] - temp[0])
    else:
        if len(temp) > 0:
            temp.append(road[i-1])
            temp.sort()
            ans.append(temp[-1] - temp[0])
            temp = []
        else:
            temp = [road[i]]

ans.sort()
print(ans[-1])