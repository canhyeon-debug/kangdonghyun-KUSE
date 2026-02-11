N, K = map(int, input().split())
results = []

for i in range(N):
    
    if N%(i+1) == 0:
       
        results.append(i+1)


if len(results) < K:
    print(0)
else:
    print(results[K-1])