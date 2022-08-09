n = 100
m = 100
T = int(input())
for tc in range(T):
    nd, md = map(int, input().split())
    if nd > md:
        m -= nd
    elif nd == md:
        pass
    else:
        n -= md
print(n)
print(m)
