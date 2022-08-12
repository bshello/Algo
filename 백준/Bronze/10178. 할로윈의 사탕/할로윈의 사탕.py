T = int(input())
for tc in range(T):
    candy, son = map(int, input().split())
    can = candy//son
    dy = candy%son
    print(f'You get {can} piece(s) and your dad gets {dy} piece(s).')