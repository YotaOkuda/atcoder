'''
<方針>
- 'Ai - i' の中央値が b となる
- 参考にした記事：https://drken1215.hatenablog.com/entry/2019/12/22/122300
'''

import statistics
import math

N = int(input())
A = list(map(int, input().split()))

# 'Ai - i' を格納するリスト
diff_list = []

# 'Ai - i' を格納していく
for i, a in enumerate(A):
    diff_list.append(a - (i + 1))

# 中央値を求める
median = math.ceil(statistics.median(diff_list))

# 悲しさの値を表す変数
ans = 0

# b = median として、悲しさの値を求める
for i, a in enumerate(A):
    ans += abs(a - (i + 1 + median))
    
print(ans)

# 計算量 O(N log N) ソートしているため