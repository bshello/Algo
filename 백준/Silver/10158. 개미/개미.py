import sys
n, m = map(int, sys.stdin.readline().split())
c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
r = m - r

i = k % (2*m)
j = k % (2*n)

if i > m + r:
    r = m - (i - m - r)
elif i > r:
    r = i - r
else:
    r -= i

if j > 2*n - c:
    c = j - (2*n - c)
elif j > n - c:
    c = n - (j - n + c)
else:
    c += j

print(c, m - r)
