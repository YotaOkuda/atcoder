'''
<方針>
- 1 ～ D ごとに、長さを k 伸ばしたときの最大値を出力する
- 最大値を max で比較し、更新していく
- k が変わったら、maxWeight を初期化
'''

N, D = map(int, input().split())
sneaks = [list(map(int, input().split())) for l in range(N)]

# 長さを 1 ～ D まで変化させていく
for i in range(1, D + 1):
    maxWeight = 0
    # 長さを i 伸ばしたときの最大値を求める
    for sneak in sneaks:
        maxWeight = max(maxWeight, sneak[0] * (sneak[1] + i))
        
    print(maxWeight)

# 計算量 O(N * D), (maxD = maxN)