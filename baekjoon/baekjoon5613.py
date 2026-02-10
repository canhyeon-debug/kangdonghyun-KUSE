results = int(input())

while True:
    M = str(input())

    if M == '=':
        break
    else :
        A = int(input())
        
        if M == '+':
            results += A
        elif M == '-':
            results -= A
        elif M == '*':
            results *=A
        elif M == '/':
            results //= A


print(results)

    
