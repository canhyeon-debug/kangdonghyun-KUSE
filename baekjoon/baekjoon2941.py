alp = str(input())
results = []

results = alp.replace('c=', '*')
results = results.replace('c-', '*')
results = results.replace('dz=', '*')
results =  results.replace('z=', '*')
results = results.replace('d-', '*')
results =  results.replace('lj', '*')
results =  results.replace('nj', '*')
results =  results.replace('s=', '*')

#문자열을 다른 문자열로 바꾸는 함수인 replace().
#어떤 문자열.replace('바꿀 문자열', '바뀐 문자열') = 새로운 리스트 --> 이런 식으로 사용.

print(len(results))


 