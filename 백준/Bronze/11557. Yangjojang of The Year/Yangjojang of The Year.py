T = int(input())
for tc in range(T):
    school = int(input())
    sch = list()
    temp = 0
    for i in range(school):
        sch.append(list(input().split()))
    for j in sch:
        if int(j[1]) >temp:
            temp = int(j[1])
    for k in sch:
        if int(k[1]) == temp:
            print(k[0])