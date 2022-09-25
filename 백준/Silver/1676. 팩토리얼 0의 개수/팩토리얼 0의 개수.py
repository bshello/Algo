n = int(input())
cnt = 0
for i in range(5, n+1, 5):
    if i % 5 == 0:
        while i % 5 == 0:
            i //= 5
            cnt += 1

print(cnt)