def facto(n):
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret

def calc(a, b):
    return facto(a) // (facto(a-b) * facto(b))

a, b = map(int, input().split())
print(calc(a,b))
