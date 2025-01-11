'''
<方針>
- 各餅(Ai)について、大きさが倍以上の餅の個数を求める
- 既にソート済みのため、Ai について大きさが倍以上の餅のうち最小のインデックスを求める
- （N - 倍以上の餅のうち最小のインデックス）が餅 Ai より大きさが倍以上の餅の個数となる
- インデックスは順に探していくと O(N^2) に近づくため、二部探索で求める
'''

import bisect

N = int(input())
A = list(map(int, input().split()))

# 個数をカウントする変数
ans = 0

# 各餅 Ai について、倍以上となる餅の個数を数える
for a in A:
    ans += N - bisect.bisect_left(A, a * 2)
    
print(ans)

# 計算量 O(NlogN)