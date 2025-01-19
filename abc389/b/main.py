'''
<方針>
- 制約の中で、N! = X を満たす N は最大でも 20
- N = 20 まで階乗を計算して、X と一致する N を出力
'''

import math
X = int(input())

for i in range(2, 21):
        if math.factorial(i) == X:
            print(i)
            break
        
# 計算量 O(1)