T = int(input())
results = []

for i in range(T):
    a ,b = map(int, input().split())
    results.append(a + b)

n = 0

for r in results:
    n = n + 1
    print('Case {}: {}'.format(n, r))