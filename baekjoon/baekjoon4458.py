N = int(input())
results = []

for i in range(N):
    english = str(input())
    results.append(english)

for r in results:
    r = r[0].upper()+r[1:]
    print(r)

