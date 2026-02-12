arr = []
re = []
ee = []

for i in range(8):
    A = int(input())
    arr.append((A, i+1))

arr.sort(reverse = True)

for j in range(5):
    summ, num = arr[j]
    re.append(summ)
    ee.append(num)

ee.sort()

print(sum(re))
print(*ee)


