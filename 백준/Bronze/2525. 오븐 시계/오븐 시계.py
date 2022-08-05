h, m = map(int, input().split())
t = int(input())
h2 = ((h*60)+m+t)//60
if h2 >= 24:
    h2 = h2-24
m2 = ((h*60)+m+t)%60
print(h2, m2)