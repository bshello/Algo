n = int(input())
sw = list(map(int, input().split()))
sn = int(input())
inp = list()
for _ in range(sn):
    x = list(map(int, input().split()))
    inp.append(x)

for _ in range(n):
    sw.append(2)

for i in range(sn):
    if inp[i][0] == 1:
        for j in range(1,n+1):
            if j%inp[i][1] == 0:
                if sw[j-1] == 0:
                    sw[j-1] = 1
                else:
                    sw[j-1] = 0
            else:
                pass
    else:
        for k in range(inp[i][1]):
            if sw[inp[i][1]+k-1] == sw[inp[i][1]-k-1]:
                if sw[inp[i][1]-k-1] == 0:
                    sw[inp[i][1] - k-1] = 1
                    sw[inp[i][1] + k-1] = 1

                else:
                    sw[inp[i][1] - k-1] = 0
                    sw[inp[i][1] + k-1] = 0
            else:
                break
cnt = 0
for q in range(n):
    cnt+=1
    print(sw[q], end = " ")
    if cnt == 20:
        print("")
        cnt = 0
