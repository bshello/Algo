T = int(input())
n = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in n:
    if v == i:
        cnt+=1
print(cnt)