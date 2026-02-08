T = int(input())

for i in range(T):
    N, D = map(int, input().split())
    spaceship = []
    for j in range(N):
        v, f, c = map(int, input().split())
        
        if v*(f/c) >= D:
            spaceship.append(1)
    print(sum(spaceship))

