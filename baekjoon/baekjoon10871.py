N, X = map(int, input().split())
results = []
seq = list(map(int,input().split()))

for i in range(N):
    if seq[i] < X:

        results.append(seq[i])

print(results[0:])