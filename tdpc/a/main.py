'''
<方針>
- dp[i][0] はi 点を取っているかを真偽値で表す
- dp[i][1] は更新対象かを表す
（i回目のループで更新されたものに対しては更新しない）
- dp[i][0] が未更新のものに対してだけ更新作業を行う
（更新済みのものを'no' にしてしまい、以降の更新に影響を及ぼすため）
'''
'''
N = int(input())
P = list(map(int, input().split()))

sum_point = sum(P)
dp = [[False, 'ok'] for _ in range(sum_point + 1)]
dp[0][0] = True

for i in range(N):
    for x in range(len(dp)):
        if dp[x][0] and dp[x][1] == 'no':
            dp[x][1] = 'ok'

    for j in range(len(dp)):
        if dp[j][0] == False and j - P[i] >= 0 and dp[j - P[i]][0] and dp[j - P[i]][1] == 'ok':
            dp[j][0] = True
            dp[j][1] = 'no'

ans = 0
for point in dp:
    if point[0]:
        ans += 1

print(ans)
'''

# 計算量 O(N * sum(P)) = O(10^6)


# リファクタリング
'''
<方針>
- 各P[i]に対応するdp[i]を作成する
- dp[i][j]に対して、dp[i-1][j]がTrueの場合
  1. 選ばないdp[i][j] = True
  2. 選ぶdp[i][j+P[i-1]] = True
'''
N = int(input())
P = list(map(int, input().split()))

dp = [[False] * 10001 for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(10001):
        if dp[i-1][j]:
            dp[i][j] = True
            dp[i][j+P[i-1]] = True

ans = sum(dp[-1])

# 計算量 O(N * 10001) = O(10^6)
print(ans)
