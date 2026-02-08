S = str(input())
alpabets = 'abcdefghijklmnopqrstuvwxyz'
results = [0]*len(alpabets)

for i in S:
    for j in range(len(alpabets)):
        if i == alpabets[j]:
            results[j]+=1

print(*results)