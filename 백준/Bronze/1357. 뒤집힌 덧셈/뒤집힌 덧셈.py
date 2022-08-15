def rev(x):
    a = list(str(x))
    a.reverse()
    b = ''.join(a)
    return int(b)

n, m = map(int, input().split())

ans = rev(rev(n) + rev(m))
print(ans)
