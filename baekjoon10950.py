T = int(input())
results = []

for i in range(T):
    a, b = map(int, input().split())
    results.append(a + b)

for j in results:
    print(j)