N = int(input())

score = list(map(int, input().split()))
results = []

for s in score:
    results.append((s/max(score))*100)

print(sum(results)/N)