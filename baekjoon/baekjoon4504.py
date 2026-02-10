n = int(input())

while True:
    a = int(input())
    if a % n == 0 and not a == 0:
        print('{} is a multiple of {}.'.format(a, n))
    elif a  == 0:
        break
    else:
        print('{} is NOT a multiple of {}.'.format(a, n))

   