T = int(input())


for i in range(T):
    n = int(input())
    binary = format(n, 'b')
    results = []
    for j in range(len(binary)):
        
        if binary[-1*(j+1)] == '1':
            results.append(j)
            
    print(*results)

