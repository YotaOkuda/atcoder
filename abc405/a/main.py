'''
<方針>
- div によって、それぞれレート範囲化を判定する
'''
R, X = map(int, input().split())

if X == 1:
    if 1600 <= R <= 2999:
        print('Yes')
    else:
        print('No')
else:
    if 1200 <= R <= 2399:
        print('Yes')
    else:
        print('No')

# 計算量 O(1)
