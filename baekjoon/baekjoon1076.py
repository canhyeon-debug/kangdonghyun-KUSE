F = input()
S = input()
T = input()

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

first = color.index(F)
second = color.index(S)
third = color.index(T)

print((10*first+second)*(10**third))