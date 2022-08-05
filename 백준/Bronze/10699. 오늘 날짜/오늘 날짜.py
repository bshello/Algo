from datetime import datetime

y = datetime.today().year  
m = datetime.today().month 
d = datetime.today().day
if m <10:
    k = '0'+str(m)
if d <10:
    l = '0'+str(d)
print(f'{y}-{k}-{l}')  