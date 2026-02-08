results = []

for i in range(5):
    A = int(input())
    results.append(A)

for j in range(4):
    results[j+1]=results[j+1]+results[j]

print(results[4])