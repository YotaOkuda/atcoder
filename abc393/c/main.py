'''
<方針>
- グラフを単純化するには以下の 2 通りの場合にグラフから除外（そもそも追加しない）すればよい
  1. 自己ループのとき（u, v の値が一致している場合）
  2. 辺が重複しているとき（追加する u, v が既にグラフ G に存在している場合）
- 重複しているかセットで管理することでより高速に
'''

N, M = map(int, input().split())

count = 0
# リファクタリング前
'''
G = [[] for _ in range(N)]
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1

  # 1 の場合
  if u == v:
    count += 1
  # 2 の場合
  elif (u in G[v]) & (v in G[u]):
    count += 1
  else:
    G[u].append(v)
    G[v].append(u)
'''

# リファクタリング後
graph = set()
for i in range(M):
  u, v = map(int, input().split())
  if u == v:
    count += 1
  elif (u, v) in graph or (v, u) in graph:
    count += 1

  graph.add((u, v))

print(count)

# 計算量 O(M)