N =int(input())

num = 1

if N == 0:
    num = 1
else: 
    for i in range(1, N+1):

        num = num * i
   
    

fac = list(str(num))

count = 0

#리스트 만들때는 list = [] 이렇게 정의하고
#변수를 처음 만들때는 example = 0 이렇게 정의하고 시작하자!

for j in range(len(fac)):
    
    if fac[-1*(j+1)] == '0':
        count += 1
        
    else : 
        break

print(count)