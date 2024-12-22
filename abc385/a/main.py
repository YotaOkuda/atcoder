'''
<方針>
- A, B, C が全て等しい場合
- 足し合わせた 2 つの数が残りの 1 つに等しくなる場合 を計算する
'''

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

# 計算量 O(1)