a = int(input())


for i in range(a):
    num = list(map(int, input().split()))
    results = []
    for j in num:
        if j%2 == 0:
            results.append(j)
            

    print(sum(results), min(results))