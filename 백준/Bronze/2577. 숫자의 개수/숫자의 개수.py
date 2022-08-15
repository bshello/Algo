inp = list()
for _ in range(3):
    inp.append(int(input()))
s = 1
for i in inp:
    s *= i
num = list(str(s))
ans = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for j in num:
    if j in ans:
        ans[j] += 1
for k in ans.values():
    print(k)