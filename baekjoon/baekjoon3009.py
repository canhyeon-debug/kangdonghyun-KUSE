x_list = []
y_list = []

for _ in range(3):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)

for x in x_list:
    if x_list.count(x) == 1:
        xresult = x

for y in y_list:
    if y_list.count(y) == 1:
        yresult = y

print(xresult, yresult)

#XOR로 풀기
#a, b = map(int, input().split())
#c, d = map(int, input().split())
#e, f = map(int, input().split())

#print("{} {}".format(a^c^e,b^d^f))