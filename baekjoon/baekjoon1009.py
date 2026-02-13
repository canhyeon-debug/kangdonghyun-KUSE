import math

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = str(pow(a, b, 10))
    if c[-1] == '0':
        print(10)
    else: 
        print(c[-1])
