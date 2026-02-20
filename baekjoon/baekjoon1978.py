N = int(input())
sosu = list(map(int, input().split()))
results = []


for s in sosu:
    if s == 1:
        continue

    is_prime = True
    for i in range(2, int(s**0.5) + 1):
        if s % i == 0:
            is_prime = False
            break

    if is_prime:
        results.append(s)

print(len(results))