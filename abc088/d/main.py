'''
<方針>
- (0, 0) から (H-1, W-1) まで最短で到達可能な白の個数を求める
  全体の白の個数 - 最短の道の白の個数 = 黒に塗り替えられる「最大数」
- (0, 0) からの幅優先探索で (H-1, W-1) までの最短の白の個数を求める
'''

from queue import Queue

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 幅優先探索
def bfs(start):
    # 探索リストを定義
    que = Queue()
    # dist[0][0] からの最短経路長を表す
    dist = [[-1] * W for _ in range(H)]
    
    # 最初に始点 [0, 0] を探索リストにセット、最短経路長を 0 にセット
    que.put(start)
    dist[start[0]][start[1]] = 0
    
    # マス間の移動を定義（上、右、下、左）
    move_H = [-1, 0, 1, 0]
    move_W = [0, 1, 0, -1]
    
    # 探索リストが空になるまで、探索する
    while not que.empty():
        # 対称のマスを取り出す
        v = que.get()
        
        # v から移動できるマスを探索
        for h, w in zip(move_H, move_W):
            # 移動先のマス
            next_h = v[0] + h
            next_w = v[1] + w
            
            # 移動先のマスが盤面内か判定
            if 0 <= next_h <= (H - 1) and 0 <= next_w <= (W - 1):
                # 探索済みならスキップ
                if dist[next_h][next_w] != -1:
                    continue
                
                # 未探索かつ白のマスなら、探索リストに追加し、最短経路長を更新
                if S[next_h][next_w] == '.':
                    que.put([next_h, next_w])
                    dist[next_h][next_w] = dist[v[0]][v[1]] + 1
    
    return dist


# 最短経路長を受け取る
dist = bfs([0, 0])

# (H-1, W-1) マスに到達不可能なら -1 を出力
if dist[H - 1][W - 1] == -1:
    print(-1)
# 到達可能なら、全体の白の数 - 最短経路長 を出力
else:
    white_count = 0
    for s in S:
        white_count += s.count('.')
        
    print(white_count - dist[H - 1][W - 1] - 1)

# 計算量 O(H * W)