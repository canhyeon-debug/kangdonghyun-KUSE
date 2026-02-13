num = list(str(input()))

num.sort(reverse=True)
results = "".join(num)
print(results)

#join은 리스트 안에 있는 요소들을 공백없이 붙여주는 역할을함.
#하지만 새로운 리스트를 만들어서 공백이 없는 문자열을 갖게 해야함.
# example_list = "".join(공백이 있는 리스트 이름)