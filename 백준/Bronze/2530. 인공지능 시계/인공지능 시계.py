h, m, s = map(int, input().split())
t = int(input())
time = h*3600+m*60+s+t
h2 = time//3600
while h2>=24:
    h2 -= 24
m2 = (time%3600)//60
s2 = (time%3600)%60
print(h2, m2, s2)