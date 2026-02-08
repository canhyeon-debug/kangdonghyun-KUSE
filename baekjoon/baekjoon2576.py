m = []
n = []

for i in range(7):
    num = int(input())

    if num%2 == 0:
        m.append(num)
    else :
        n.append(num)
 
if len(m) == 7:
    print(-1)
else:
    print(sum(n))
    print(min(n))
