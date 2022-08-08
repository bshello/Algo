T = int(input())
co = {'Q1': 0, 'Q2':0,'Q3':0,'Q4':0, 'AXIS':0}
for tc in range(T):
    x,y = map(int, input().split())   
    if x == 0 or y == 0:
        co['AXIS'] += 1
    elif x>0 and y>0:
        co['Q1'] += 1
    elif x<0 and y>0:
        co['Q2'] += 1
    elif x<0 and y<0:
        co['Q3'] += 1
    else:
        co['Q4'] += 1

q1 = co['Q1']
q2 = co['Q2']
q3 = co['Q3']
q4 = co['Q4']
axis = co['AXIS']

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')