'''
<方針>
- DP で解く
- dp[n] は n 円の最小引き出し回数を表す
- ボトムアップに遷移回数を計算していく
- 1, 6, 9, 36, ..., と合計で 12 種類の引き出し方のみになる
- dp[n] = min(dp[n], dp[n - x] + 1) となる
  - （例）n = 7, x = 6 の場合、dp[7] = min(dp[7], dp[1] + 1)
    7 円を引き出す場合、1 + 6 となるように、取りうる遷移幅 x の内最小値を求める
'''

N = int(input())

# 十分に大きい値
INF = 110000
# dp 用の配列
dp = [INF] * (N + 1)
# 初期値
dp[0] = 0

# 6, 9, それぞれの累乗を配列に格納しておく
pow6, pow9 = [], []
base6, base9 = 1, 1
while base6 <= N:
    pow6.append(base6)
    base6 *= 6
while base9 <= N:
    pow9.append(base9)
    base9 *= 9

# ボトムアップに dp[i] を計算していく
for i in range(1, N + 1):
    # とりうる x のうち、最小回数となる組み合わせを求める
    for x in pow6:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)
    for y in pow9:
        if i - y >= 0:
            dp[i] = min(dp[i], dp[i - y] + 1)
        
print(dp[N])

# 計算量 O(N)