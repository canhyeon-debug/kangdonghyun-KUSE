N = int(input())

i = 1 #i 초기값 설정
count = 0 #count 정의

while N > 0: # N이 0보다 작거나 같은 경우는 False이므로 while문 작동안함.
    if i > N:
        i = 1 # N-i<0이면 i값 1로 초기화하고 밑에 코드 계속 진행함

    N -= i
    count += 1
    i += 1

print(count) # N이 0보다 작거나 같은 경우는 바로 여기로 이동해서 작동.


    
  