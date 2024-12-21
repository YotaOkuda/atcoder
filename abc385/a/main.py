A, B, C = map(int, input().split())

if A == B == C:
    print('Yes')
elif A == (B + C):
    print('Yes')
elif B == (A + C):
    print('Yes')
elif C == (A + B):
    print('Yes')
else:
    print('No')