N = int(input())
cnt = 0
while N % 5 != 0 and N > 2:
    N -= 3
    cnt += 1

if N % 5 == 0:
    cnt += N//5
else:
    cnt = -1

print(cnt)
