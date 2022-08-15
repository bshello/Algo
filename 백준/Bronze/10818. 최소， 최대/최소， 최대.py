T = int(input())
n = list(map(int, input().split()))
mi = 1000000
ma = -1000000
for i in n:
    if ma < i:
        ma = i
    if mi > i:
        mi = i
print(mi, ma)