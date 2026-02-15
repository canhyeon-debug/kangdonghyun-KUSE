word = input()

if word in [0,1,2,3,4,5,6,7,8,9]:
    num = int(word)
    print(chr(num))
else :
    print(ord(word))
