a = int(input())
b = list(map(int,input()))
b.reverse()
num = []

for i in b:
    print(i*a)
    num.append(i*a)
print(num[0]+(num[1]*10)+(num[2]*100))