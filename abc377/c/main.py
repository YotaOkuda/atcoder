'''
<方針>
- 盤面を作ると、N が大きすぎるため、O(N^2) は TLE となる
- ナイトの位置と移動先を重複がないようにカウントし、全体のマス数から引く
- M 個のコマを処理するだけなら、O(M) で間に合う
'''

N, M = map(int, input().split())

# コマの位置と移動先を格納する
set = set()

# コマの動きを定義
move_i = [2, 1, -1, -2, -2, -1, 1, 2]
move_j = [1, 2, 2, 1, -1, -2, -2, -1]

# 各コマに対して、位置と移動先を決めていく
for _ in range(M):
    a, b = map(int, input().split())
    
    # コマの位置を追加
    set.add((a, b))
    
    # コマの移動先を追加
    for i, j in zip(move_i, move_j):
        # 移動先が盤上内か確認する
        if 1 <= a + i <= N and 1 <= b + j <= N:
            set.add((a + i, b + j))

# マス数からコマの位置と移動先を引く
print(N*N - len(set))

# 計算量 O(M)