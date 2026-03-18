import sys
input = sys.stdin.readline

N = int(input())
ans = [0]*N
A = list(map(int,input().split()))
stack = [] ##스택엔 인덱스 번호가 들어가지 실제 오큰수 값이 있진 않음.

for i in range(N):
    while stack and A[stack[-1]] < A[i]:##A[stack] -> 스택을 리스트에 넣어야 실질적인 오큰수 값이 나옴.
        ans[stack.pop()] = A[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

print(*ans)