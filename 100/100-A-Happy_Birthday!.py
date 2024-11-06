'''
<方針>
- A, B のどちらも、8 以下であれば成立する
- A + B <= 16 なので、どちらかが 8 より大きいか判定すればよい
'''

A, B = map(int, input().split())

# どちらかが 8 より大きいか判定する
if A > 8 or B > 8:
    print(':(')
else:
    print('Yay!')
    
# 計算量 O(1)