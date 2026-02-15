T = int(input())
num = []
count = 0

for i in range(T):
    N = int(input())
    num.append(N)

for n in num:
    if not n%2 == 0:
        count+=1

print(count)