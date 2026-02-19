T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    count = 1
    for j in range(1, W+1):
       
       if N <= H:
           print(100*N+count)
           break
       elif N > H:
           N -= H
           count += 1
           continue

    

