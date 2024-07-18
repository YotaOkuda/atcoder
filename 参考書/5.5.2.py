# 無向グラフ

# N(頂点数)，M(辺の数)
N, M = map(int, input().split())

G = [[] for i in range(N)]  # 頂点数Nのグラフを定義

# M本の辺を受け取る
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 有向グラフの場合はいらない

print(G)