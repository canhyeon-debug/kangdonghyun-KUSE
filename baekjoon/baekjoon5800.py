K = int(input())

for i in range(K):
    A = list(map(int, input().split()))
    scores = A[1: ]
    scores.sort(reverse = True)

    gap = []

    for j in range(len(scores)-1):
        gap.append(scores[j] - scores[j+1])





    print('Class {}'.format(i+1))
    print('Max {}, Min {}, Largest gap {}'.format(max(scores), min(scores), max(gap)))
