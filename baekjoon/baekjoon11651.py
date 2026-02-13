N = int(input())
coor = []
results = []

for i in range(N):
    x, y = map(int, input().split())
    coor.append((y, x))

coor.sort()

for c in coor:
    a, b = c
    a, b = b, a
    f = a, b
    results.append(f)


for r in results:
    print(*r)
    