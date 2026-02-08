T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    N.sort()
    
    #print(*N)
    
    #print(N.sort())
    # sort따로 하고 프린트 하기!
    
    if N[3] - N[1] < 4:
       print(sum(N[1:4]))
    else :
       print('KIN')






