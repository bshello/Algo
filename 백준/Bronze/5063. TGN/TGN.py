T = int(input())
for tc in range(T):
    r, e, c = map(int, input().split())
    m = e-c
    if r>m:
        print("do not advertise")
    elif r==m:
        print("does not matter")
    else:
        print("advertise")