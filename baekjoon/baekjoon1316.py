import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    word = list(str(input()))
    check = set()

    check.add(word[0])

    for i in range(1, len(word)):
        
        if word[i] != word[i-1] and word[i] in check:
            N -= 1  
            break
        
        
        check.add(word[i])

print(N)