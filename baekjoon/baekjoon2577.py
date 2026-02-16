A = int(input())
B = int(input())
C = int(input())
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

times = A*B*C

numbers = list(str(times))

for i in arr:
    count = 0
    for n in numbers:
        if n == i:
            count += 1
        else:
            continue
    
    print(count)