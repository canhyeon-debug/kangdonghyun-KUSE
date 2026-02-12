import sys
input = sys.stdin.readline

# int는 입력 받을 때 여러 요소를 고려하기 때문에 느리다.
# 그래서 sys 모듈 사용. 
# sys 묘듈이란 파이썬이 실행될 때 사용하는 시스템 관련 기능들을 모아둔 기능.

N = int(input())
list = []

for _ in range(N):
    list.append(int(input()))
    
list.sort()

for l in list:
    print(l)