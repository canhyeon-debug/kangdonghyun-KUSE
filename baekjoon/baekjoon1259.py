import math



while True:
    num = str(input())

    a = []

    if num == '0':
        break

    for i in range(math.ceil(len(num)/2)):
        if num[i] == num[-(i+1)]:
            a.append(1)

    if sum(a) == math.ceil(len(num)/2):
        print('yes')
    else:
        print('no')
