N = int(input())
coor = []

for i in range(5):
     x, y = map(int, input().split())
     coor.append((x, y))

coor.sort()

for c in coor:
     print(*c)
