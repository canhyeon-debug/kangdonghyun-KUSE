A, B, C = map(int, input().split())

if A<B<C or C<B<A:
    print(B)
elif C<A<B or B<A<C:
    print(A)
elif A == B or A == C:
    print(A)
elif B == C or A==B==C:
    print (B)
else :
    print(C)