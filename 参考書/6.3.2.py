from queue import Queue

# グラフ G に対して、頂点 s を始点とした幅優先探索を行う
# 返り値 : 各頂点への頂点 s からの最短距離を表す配列
def bfs(G, s):
    # todoリストを表すキュー
    que = Queue()
    
    # dist[v]は始点 s から頂点 v への最短経路長
    dist = [-1] * len(G)
    
    # 最初に始点 s を todoリストにセットする
    que.put(s)
    dist[s] = 0
    
    # todoリストが空になるまで探索する
    while not que.empty():
        # todoリストから頂点 v を取り出す
        v = que.get()
        
        # v に直接つながる頂点を探索
        for v2 in G[v]:
            # v2 がすでに探索済みの場合はスキップする
            if dist[v2] != -1:
                continue
            
            # v2 を新たに todoリストに追加
            que.put(v2)
            
            # v2 の dist の値を更新
            dist[v2] = dist[v] + 1
            
    # 最短経路長を表す配列を返す
    return dist