a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            
            # 이 문제는 수학 연산 문제가 아니라 완전 탐색 문제다!

