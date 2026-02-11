homework = []
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in range(28):
    num = int(input())
    homework.append(num)

#for h in homework:
#    if h not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
#        results.append(h)

results = [x for x in a if x not in homework]
results.sort()

for r in results:
    print(r)