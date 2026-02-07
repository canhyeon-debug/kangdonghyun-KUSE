
results = []

while True:
    M, F = map(int, input().split())
    
    if M == 0 and F == 0:
        break
    results.append(M + F)



for i in results:
    print(i)
