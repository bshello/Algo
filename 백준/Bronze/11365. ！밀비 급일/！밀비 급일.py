while True:
    n = list(input())
    if n == ['E', 'N', 'D']:
        break
    n.reverse()
    ans = ''.join(n)
    print(ans)
