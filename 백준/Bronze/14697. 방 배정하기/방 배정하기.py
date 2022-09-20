a, b, c, student = map(int, input().split())
n = student//a
ans = 0
for i in range(n+1):
    if ans == 1:
        break
    x = a * i
    m = ((student - x) // b) + 1
    for j in range(m):
        if ans == 1:
            break
        y = b * j
        l = (student - x - y) // c + 1
        for k in range(l):
            z = c * k
            if x + y + z == student:
                ans = 1
                break
print(ans)