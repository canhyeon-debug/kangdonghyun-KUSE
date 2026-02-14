x, y, w, h = map(int, input().split())

coor = [x, y, w-x, h-y]

print(min(coor))