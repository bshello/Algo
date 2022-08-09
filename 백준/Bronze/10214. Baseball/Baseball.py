T = int(input())
for tc in range(T):
    yonsei = 0
    korea = 0
    for i in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if yonsei > korea:
        print("Yonsei")
    elif yonsei == korea:
        print("Draw")
    else:
        print("Korea")