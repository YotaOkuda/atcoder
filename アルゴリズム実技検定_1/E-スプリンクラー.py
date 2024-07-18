N, M, Q = map(int, input().split())

G = [[] for i in range(N)]

# 無向グラフの作成
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v)
    G[v-1].append(u)

C = list(map(int, input().split()))     # 色のリスト

ans = []

# クエリ処理
for i in range(Q):
    s = list(map(int, input().split()))     # クエリ入力
    if s[0] == 1:               # クエリが1型
       ans.append(C[s[1]-1])    # 頂点xの現在の色を出力
       for i in G[s[1]-1]:      # スプリンクラー起動
           C[i-1] = C[s[1]-1]   # 隣接する頂点の色を現在の頂点の色に変更
    elif s[0] == 2:             # クエリが2型
        ans.append(C[s[1]-1])   # 頂点xの現在の色を出力
        C[s[1]-1] = s[2]        # 頂点xをyの色にする

# 答え出力
for i in ans:
    print(i)
