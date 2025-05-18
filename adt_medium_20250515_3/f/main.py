'''
<方針>
- Bit全探索で解く
- 最初に販売しているポップコーンの種類M を各N ごとにリスト化する
- Bit全探索で選ばれた売り場N で扱っているポップコーンM をset で管理
  選ばれた回数count を更新する
  全ての種類を満たしているならans を更新する
'''
N, M = map(int, input().split())

# 各N が扱っているポップコーンの種類のリスト
popcorns = []
for i in range(N):
    S = str(input())
    tmp = []
    for i in range(M):
        if S[i] == 'o':
            tmp.append(i)
    popcorns.append(tmp)
    
# 初期値を設定
ans = 100
# Bit全探索
for i in range(1<<N):
    # 選ばれた場所のポップコーンの種類
    tmp_popcorns = set()
    # 選ばれた場所の数
    count = 0

    # 場所N を選ぶか
    for shift in range(N):
        if 1 & (i>>shift):
            # 場所 N を選ぶならポップコーンの種類を追加する
            tmp_popcorns.update(popcorns[shift])
            count += 1

    # 全種類のポップコーンを満たしているか
    if tmp_popcorns == set(range(0, M)):
        ans = min(ans, count)

print(ans)

# 計算量 O(N^2 * N * M)
