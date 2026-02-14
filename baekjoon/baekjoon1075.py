N = int(input())
F = int(input())

num = N//100 * 100

for i in range(100):
    if (num+i)%F == 0:
        print(f"{i:02d}")
        #print(f"{변수:abc}") -> f-string
        #f-string은 문자열에 어떤 변수를 바로 넣음.
        #{값:옵션} 값은 출력할 어떤 변수고 옵션 중 b는 문자열 자릿수를 고정시킴.
        #a는 빈칸이 있을때 빈칸을 채울 변수
        #c는 채울 변수가 정수형인지 뭔지 정하는 거임.
        break

