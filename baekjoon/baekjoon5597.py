homework = []
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in range(28):
    num = int(input())
    homework.append(num)

results = [x for x in a if x not in homework]
#두 개의 리스크 비교해서 없는 거 빼는 방법?
#ex) list1 = [1, 2, 3], list2 = [1, 2]
#근데 나는 list1에서 list2의 요소를 뺀 리스트를 갖고싶다?
#print(list1 - list2) --> 이렇게 하면 오류남 ㅇㅇ
# results = [x for x in list1 if not in list2] = [3]
results.sort()

for r in results:
    print(r)