import sys
input = sys.stdin.readline
##시간 절약 모듈

N, M = map(int, input().split())
num = [[0]*(N+1)]
sum = [[0]*(N+1) for _ in range(N+1)]


for _ in range(N):
    num.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + num[i][j]

for _ in range(M):
    a, b, c, d = map(int, input().split())
    print(sum[c][d]-sum[a-1][d] - sum[c][b-1] + sum[a-1][b-1])


