import sys
input = sys.stdin.readline

N = int(input())
w = []

for _ in range(N):
    a = str(input())
    if a not in w:
        w.append(a)


w.sort(key=lambda a:(len(a), a))

for words in w:
    print(words)
