'''
<方針>
- 平均を計算して ceil で切り上げを行う
'''

import math as m

a, b = map(int, input().split())

x = m.ceil((a + b)/2)

print(x)

# 計算量 O(1)