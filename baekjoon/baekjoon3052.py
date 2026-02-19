namuzi = []

for i in range(10):
    num = int(input())

    if num%42 not in namuzi:
        namuzi.append(num%42)
    else:
        continue

print(len(namuzi))
