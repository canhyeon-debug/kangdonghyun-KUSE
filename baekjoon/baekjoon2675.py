T = int(input())

for i in range(T):
    num, word = input().split()
    num = int(num)
    results = []

    for j in range(len(word)):
        results.append(word[j]*num)

    print(''.join(results[0:]))