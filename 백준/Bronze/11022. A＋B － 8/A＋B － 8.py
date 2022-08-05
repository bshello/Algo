T = int(input())
ans = 0
for tc in range(1,T+1):
    a,b = map(int, input().split())
    ans = a+b
    print(f'Case #{tc}: {a} + {b} = {ans}')