results = int(input())
#input으로 입력받은 변수는 초기화해서 다시 사용 가능 함을 잊지말자!
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

    
