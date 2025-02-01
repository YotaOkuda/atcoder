'''
<方針>
- 方角とその対となる方角を辞書として定義して、出力する
'''

D = str(input())

opposite_direction = {'N': 'S', 'E': 'W', 'W': 'E', 'S': 'N', 
                      'NE': 'SW', 'NW': 'SE', 'SE': 'NW', 'SW': 'NE'}

print(opposite_direction[D])

# 計算量 O(1)