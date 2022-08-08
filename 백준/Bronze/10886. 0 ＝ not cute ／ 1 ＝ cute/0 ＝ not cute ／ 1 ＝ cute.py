T = int(input())
vote = list()
for tc in range(T):
    x = int(input())
    vote.append(x)
a = list()
b = list()
a.append(0)
for i in range(1,T):
    if vote[i] in a:
        a.append(vote[i])
    else:
        b.append(vote[i])
if len(a)-1>len(b):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
    