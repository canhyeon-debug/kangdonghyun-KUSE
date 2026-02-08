a = int(input())


for i in range(a):
    num = list(map(int, input().split()))
    results = []
    #리스트를 어디에 두느냐에 따라 초기화 여부가 달라진다!

    for j in num:
        if j%2 == 0:
            results.append(j)

    print(sum(results), min(results))
    #sum함수는 괄호 안에 있는 요소들은 합쳐주는 함수