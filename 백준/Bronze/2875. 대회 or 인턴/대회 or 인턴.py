f, m, intern = map(int, input().split())
cnt = 0
for i in range(1,m+1):
    a = i
    b = 2 * i
    if b <= f and a + b + intern <= f + m:
        cnt += 1
print(cnt)