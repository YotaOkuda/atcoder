'''
<方針>
- N <= 2 * 10^5 なので全探索可能
- 仮想配列で各数値ごとの最大のインデックスを記録する（アクセスも容易）
'''

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 仮想配列
num = defaultdict(int)

ans = []
# 正数列 A に対して、インデックスと要素ごとに処理する
for i, a in enumerate(A):
    # 要素のインデックスが仮想配列に記録されていない場合（初見の場合）
    if not num[a]:
        ans.append(-1)
    # インデックスが記録されている場合、そのインデックスを答えに追加
    else:
        ans.append(num[a])
    
    # 要素のインデックスを更新
    num[a] = i + 1  # 1 始まりに合わせる
    
print(' '.join(map(str, ans)))

# 計算量 O(N)