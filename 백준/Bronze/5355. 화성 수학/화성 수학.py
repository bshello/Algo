T = int(input())
for tc in range(T):
    lst = list(input().split())
    num = float(lst[0])
    a = lst[1]
    
    if len(lst)>3:
        b = lst[2]
        c = lst[3]
        if a == '@':
            num = num*3
            if b == '@':
                num = num*3
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            elif b == '%':
                num += 5
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            else:
                num -=7
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
        elif a == '%':
            num += 5
            if b == '@':
                num = num*3
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            elif b == '%':
                num += 5
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            else:
                num -=7
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
        elif a == '#':
            num -=7
            if b == '@':
                num = num*3
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            elif b == '%':
                num += 5
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
            else :
                num -=7
                if c == '@':
                    num = num*3
                elif c == '%':
                    num += 5
                else:
                    num -=7
       
    elif len(lst)>2:
        b = lst[2]
        if a == '@':
            num = num*3
            if b == '@':
                num = num*3
            elif b == '%':
                num += 5
            else :
                num -=7
        elif a == '%':
            num += 5
            if b == '@':
                num = num*3
            elif b == '%':
                num += 5
            else :
                num -=7
        else :
            num -=7
            if b == '@':
                num = num*3
            elif b == '%':
                num += 5
            else :
                num -=7
    else:
        if a == '@':
            num = num*3           
        elif a == '%':
            num += 5       
        else :
            num -=7
            
    print(format(num, ".2f"))
