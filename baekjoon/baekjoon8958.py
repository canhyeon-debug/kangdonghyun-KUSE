T = int(input())

for i in range(T):
    results = list(str(input()))
    score = 0
    k = 1
    for r in results:
        if r == 'O':
            score += k
            k +=1
        else:
            k = 1
    print(score)

