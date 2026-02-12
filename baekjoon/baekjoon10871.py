N, X = map(int, input().split())
results = []
seq = list(map(int,input().split()))

for i in range(N):
    if seq[i] < X:

        results.append(seq[i])

print(*results)

#리스트에 있는 요소만 빼려면 앞에 *붙이면 됌.