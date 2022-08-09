T = int(input())
a = 0
b = 0
c = 0
while T>9:
    if T>=300:
        c = T//300
        T = T%300
    else:
        if T>=60:
            b = T//60
            T = T%60
        else:
            if T>=10:
                a = T//10
                T = T%10

if T == 0:
    print(f'{c} {b} {a}')
else:
    print(-1)