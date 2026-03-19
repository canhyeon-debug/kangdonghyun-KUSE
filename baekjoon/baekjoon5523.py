import sys
input = sys.stdin.readline

N = int(input())
awin = 0
bwin = 0

for _ in range(N):
    a, b = map(int,input().split())
    if a>b:
        awin += 1
    elif a<b:
        bwin += 1
    else:
        continue

print('{} {}'.format(awin, bwin))
