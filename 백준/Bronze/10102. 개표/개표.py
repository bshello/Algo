num = int(input())
vote = list(input())
a = list()
b = list()
a.append(vote[0])
for i in range(1,num):
    if vote[i] in a:
        a.append(vote[i])
    else:
        b.append(vote[i])
if len(a)>len(b):
    print(a[0])
elif len(a)==len(b):
    print("Tie")
else:
    print(b[0])