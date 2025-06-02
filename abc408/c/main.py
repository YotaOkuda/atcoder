'''
<方針>
- 単純に範囲を加算していく場合は、O(N * M) となりTLE
- いもす法を使って解いていく
'''

N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

wall = [0] * N
for i in range(M):
    L, R = LR[i][0] - 1, LR[i][1] - 1
    # 開始範囲を +1 する
    wall[L] += 1
    # 終了範囲の次を -1 する
    if R + 1 < N:
        wall[R + 1] -= 1

# 最終の数え上げ
start = 0
for i in range(N):
    wall[i] = start + wall[i]
    start = wall[i]

print(min(wall))

# 計算量 O(N + M
