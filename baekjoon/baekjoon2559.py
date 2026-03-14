import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tem = list(map(int, input().split()))
result = []
sum = 0

for i in range(K):
    sum += tem[i]

result.append(sum)

for a in range(K, N):
    sum += tem[a] - tem[a-K]
    result.append(sum)

print(max(result))