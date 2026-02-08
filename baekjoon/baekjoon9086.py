T = int(input())
results = []

for i in range(T):
    A = str(input())
    results.append(A)

for j in range(T):

    print(results[j][0]+results[j][-1])
    