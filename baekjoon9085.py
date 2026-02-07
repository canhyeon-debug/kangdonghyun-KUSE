T = int(input())

for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    for j in range(N-1):
        numbers[j+1] = numbers[j+1]+numbers[j]

    print(numbers[N-1])
