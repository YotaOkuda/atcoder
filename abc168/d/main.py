'''
<方針>
- 各部屋から部屋 1 までの最短経路長を、部屋 1 を始点として幅優先探索で求める
- 部屋 v から繋がっている部屋 v2 の最短経路長を更新する場合、
  部屋 v2 に部屋 v を示す道しるべを置く
- グラフが連結なので、必ず 'Yes' になる
'''

from queue import Queue

N, M = map(int, input().split())

# 部屋を頂点とした無向グラフを作成
G = [[] for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    
    # 部屋番号を 0 始まりにそろえる
    a -= 1
    b -= 1
    
    G[a].append(b)
    G[b].append(a)
    

# 幅優先探索を行う
def bfs(G):
    # 探索リスト
    que = Queue()
    # 部屋 0 から各部屋への最短経路長を表す
    dist = [-1] * N
    # 各部屋の道しるべを表す（部屋 1 から）
    signpost = [-1] * (N - 1)
    
    # 部屋 0 を始点にセット、距離を 0 にセット
    que.put(0)
    dist[0] = 0
    
    # 部屋 v から移動できる部屋を探索
    while not que.empty():
        # 探索始点の部屋を取り出す
        v = que.get()
        
        # 部屋 v に直接繋がっている部屋を探索
        for v2 in G[v]:
            # 探索済みならスキップ
            if dist[v2] != -1:
                continue
            
            # 部屋 v2 を新たに探索リストに加える
            que.put(v2)
            # 最短経路長を更新
            dist[v2] = dist[v] + 1
            # 道しるべを更新（出力用に部屋を 1 始まりとして考える）
            signpost[v2 - 1] = v + 1
            
    return signpost


signpost = bfs(G)
# 答えを出力
print('Yes')
for sign in signpost:
    print(sign)
    
# 計算量 O(N + M)