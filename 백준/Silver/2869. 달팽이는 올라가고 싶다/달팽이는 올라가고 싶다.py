a, b, v = map(int, input().split())

temp = v - a
if temp % (a-b) != 0:
    bonus = 2
else:
    bonus = 1
ans = (temp // (a - b))

answer = ans + bonus

print(answer)