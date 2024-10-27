'''
<方針>
ボールの種類ごとに個数を数えて、少ない個数のボールからK種類になるまで書き換える
'''

from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

num = defaultdict(int)

# 書かれている整数ごとに何個ずつあるか
# （例） 1 とかかれているボールが何個あるか
for a in A:
    num[a] += 1

# 数が少ない整数順にソート
num = sorted(num.items(), key=lambda x: x[1])
# 種類数をカウント
unique_count = len(num)
# 塗り替えるべき種類数
change_value = unique_count - K

ans = 0
# 塗り替える必要がない場合
if unique_count <= K:
    print(0)
# 塗り替える場合
else:
    # 数が少ない整数から塗り替えるべき種類数分塗り替える
    for i in range(change_value):
        # 1 種類の個数を累計していく
        ans += num[i][1]
    print(ans)
    
# 計算量 O(N logN)