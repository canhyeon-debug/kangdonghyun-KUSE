a, b, c, d, e, f = map(int, input().split())

x = ((e*c//b)-f)//((e*a//b)-d)

y = (c-(a*f//d))//(b-(a*e//d))

print('{} {}'.format(x, y))