import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0]+list(map(int, input().split()))
sum = [[0]*(N+1)]+[[0]*(N+1-a) for a in range(N)]

count = 0

#print(sum)

for i in range(1, N+1):
    for j in range(i, N+1):
            sum[i][j-(i-1)] = sum[i][j-1-(i-1)] + A[j]

print(sum)

for i in range(1, N+1):
    for j in range(1, N+2-i):
        if sum[i][j] % 3 == 0:
            count +=1
        
print(count)