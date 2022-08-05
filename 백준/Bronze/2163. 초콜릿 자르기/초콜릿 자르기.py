n, m = map(int, input().split())
if n>1 and m>1:
    if n>m:
        num = ((m-1) + (n-1)*m)
    else:
        num = ((n-1) + (m-1)*n)
elif n == 1 and m>1:
    num = m-1
elif m == 1 and n>1:
    num = n-1
else:
    num = 0
print(num)