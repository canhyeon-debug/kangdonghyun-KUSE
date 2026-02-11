M = int(input())
D = int(input())

if M == 2 and D == 18:
    print('Soecial')
elif M < 2 or M == 2 and D < 18:
    print('Before')
elif M > 2 or M == 2 and D > 18:
    print('After')