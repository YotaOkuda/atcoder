'''
<方針>
- A + B, C + D をそれぞれ計算する
- 左右の重みを比較して、適切な答えを出力
'''

A, B, C, D = map(int, input().split())

# 左の重さ
left_weight = A + B
# 右の重さ
right_weight = C + D

# 重みを比較して、適切な答えを出力
if left_weight > right_weight:
    print('Left')
elif left_weight < right_weight:
    print('Right')
else:
    print('Balanced')
    
# 計算量 O(1)