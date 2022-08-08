a = int(input())
b = input()
c = int(input())
d = ['+','*']
cnt = 0
for i in d:
    cnt+=1
    if i == b:
        break
if cnt == 1:
    print(a+c)
else:
    print(a*c)
