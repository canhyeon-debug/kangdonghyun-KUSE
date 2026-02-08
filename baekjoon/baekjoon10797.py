D = int(input())
C = list(map(int, input().split()))
num = []

for i in C:
    if D == i:  
        num.append(1)

print(sum(num))