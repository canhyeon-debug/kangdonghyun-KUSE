N = int(input())


for M in range(max(1, N-(9*len(str(N)))), N):
    if M + sum(map(int, str(M))) == N:

        print(M)
        break
        

else:
    print(0)