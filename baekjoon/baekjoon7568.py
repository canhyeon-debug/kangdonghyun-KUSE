N = int(input())
weigh = []
results = []

for i in range(N):
    x, y = map(int, input().split())
    weigh.append((x, y))


for (a, b) in weigh:
    count = 0
    for (x, y) in weigh:
        if a < x and b < y:
            count += 1
    results.append(count+1)

print(*results)