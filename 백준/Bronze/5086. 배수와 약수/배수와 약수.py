a, b = map(int,input().split())
while a != 0 and b!=0:  
    if b>a:
        if b % a == 0:
            print("factor")
        else:
            print("neither")
    else:
        if a % b == 0:
            print("multiple")
        else:
            print("neither")
    a, b = map(int,input().split())
