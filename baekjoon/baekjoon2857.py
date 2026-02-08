b = []
c = []

for i in range(5):
    a = str(input())
    if 'FBI' in a:
        b.append(i+1)
        c.append(a)
    
if any('FBI' in s for s in c):
    print(*b)
else:
    print('HE GOT AWAY!')
