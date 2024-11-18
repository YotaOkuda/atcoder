'''
<方針>
- 各頂点を始点として、幅優先探索を行う
- 距離ごとの出現頻度をカウントする
- 各距離は 2 回カウントされているので、1/2 した値を出力する
'''

from queue import Queue

N, X, Y = map(int, input().split())

# グラフ G の作成
G = [[] for _ in range(N)]
for i in range(N):
    if i == 0:
        G[i].append(1)
    elif i == N - 1:
        G[i].append(i - 1)
    else:
        G[i].append(i - 1)
        G[i].append(i + 1)

# 頂点 X, Y を繋ぐ辺をグラフ G に追加
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)

# 距離ごとの出現頻度をカウントするリスト
distanceCount = [0] * (N - 1)

# 幅優先探索
def bfs(start):
    # 探索リスト
    que = Queue()
    # 始点から各頂点への最短距離を表す
    dist = [-1] * N
    
    # 始点を探索リストに追加
    que.put(start)
    # 始点の距離を 0 にする
    dist[start] = 0
    
    # 頂点 v から移動できる頂点を探索
    while not que.empty():
        v = que.get()
        # 頂点 v から直接移動できる頂点を探索
        for v2 in G[v]:
            # 探索済みならスキップ
            if dist[v2] != -1:
                continue
            
            # 未探索なら探索リストを更新、距離を更新
            que.put(v2)
            dist[v2] = dist[v] + 1
    
    # 距離ごとの出現頻度をカウント
    for distance in dist:
        if distance == 0:
            continue
        distanceCount[distance - 1] += 1
            
    return
    

# 全頂点が始点となるように bfs を実行
for i in range(N):
    bfs(i)

# 距離ごとの出現頻度を出力（重複分は引く）
for ans in distanceCount:
    print(ans // 2)
    
# 計算量 O(N ^ 2) = O(N * (N + M)), M - 1 = N