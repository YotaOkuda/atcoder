'''
<方針>
- それぞれ計算して、最大値を出力
'''

A, B = map(int, input().split())

print(max(A + B, A - B, A * B))

# 計算量 O(1)