time = list()
for i in range(2):
    a = list(map(int, input().split(':')))
    time.append(a)

time[1][0] -= 1
time[1][1] += 59
time[1][2] += 60
time.append([0, 0, 0])

for j in range(3):
    time[2][j] = time[1][j] - time[0][j]

if time[2][2] >= 60:
    time[2][2] -= 60
    time[2][1] += 1
if time[2][1] >= 60:
    time[2][1] -= 60
    time[2][0] += 1
if time[2][0] < 0:
    time[2][0] += 24
if time[2][1] < 0:
    time[2][1] += 60

timer = list(map(str, time[2]))

if time[2][0] < 10:
    timer[0] = '0' + timer[0]
if time[2][1] < 10:
    timer[1] = '0' + timer[1]
if time[2][2] < 10:
    timer[2] = '0' + timer[2]

print(f'{timer[0]}:{timer[1]}:{timer[2]}')
