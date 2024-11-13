'''
<方針>
参考URL：https://drken1215.hatenablog.com/entry/2018/08/05/224100
- 問題の種類が 1 <= D <= 10 と最大 10 種類なので、問題の種類ごとに全完するか探索する
  ビット全探索で探索をする
- 全完してもスコアを満たさない場合は、全完対象外の問題を点数の高い順に 1 問ずつ解いていく
'''

D, G = map(int, input().split())
P, C = [], []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

# 解いた問題数（初期値は合計問題数より大きい値にしておく）
ans = 2000

# ビット全探索（問題の種類を 1 bit として）
for num in range(1<<D):
    # 合計スコア、解いた問題数を格納する変数
    score, count = 0, 0
    
    # 全完する組み合わせの総スコアを求める
    for shift in range(D):
        # その点数の問題を全完する場合
        if 1 & (num>>shift) == 1:
            score += (shift + 1) * 100 * P[shift] + C[shift]
            count += P[shift]
    
    # 全完してもスコアに届かない場合
    if score < G:
        score, count = 0, 0
        # 全完対象外の問題を点数の高い順に 1 問ずつ解いていく
        for shift in range(D - 1, -1, -1):
            if 1 & (num>>shift) == 0:       # 0 は全完対象外を表す
                for i in range(P[shift]):
                    # スコアを満たしたら終了
                    if score >= G:
                        break
                    score += (shift + 1) * 100
                    count += 1
                # 対象の種類の問題を解き切ったらボーナスを追加
                if i == P[shift] - 1:
                    score += C[shift]
    
    # スコアを満たしているなら、最小回数を比較して更新
    if score >= G:
        ans = min(ans, count)

print(ans)

# 計算量 O(2^D * D)