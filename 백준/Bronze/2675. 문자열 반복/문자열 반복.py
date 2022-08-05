T = int(input())
for tc in range(T):
    lst = []
    num, sen = input().split()
    for i in range(len(sen)):
        for j in range(int(num)):
            lst.append(sen[i])
    for k in lst:
        print(k, end="")
    print("")