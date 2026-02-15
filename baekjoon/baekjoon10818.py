N = int(input())

int_number = list(map(int, input().split()))

# map은 꼭 변수에 넣거나 리스트로 변환해야 출력가능함!
# a, b = map(~,~) 또는 example = list(map(~,~)) --> 이런 식으로 ㅇㅇ
# 리스트로 변환할때는 꼭 'list()' 함수를 써줘야함.
# example = [], example = map(~,~) 이런 식으로 빈 공간 만들어서 하면 계산 꼬임.

print('{} {}'.format(min(int_number), max(int_number)))