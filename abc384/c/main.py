'''
<方針>
- 問題の組み合わせをビット全探索する
- shift 回数と問題を対応させ、解いた問題の文字列を作る
- 文字列とスコアをペアで記録していく
- スコアを基準として降順にソート、同スコアの場合は辞書順で小さくなるように
'''

score_list = list(map(int, input().split()))
# moji_list の順になるよう、スコアを逆順にする
score_list = list(reversed(score_list))
# 各問題の文字を格納するリスト
moji_list = ['E', 'D', 'C', 'B', 'A']

# スコアと文字列を記録するリスト
ans = []
# ビット全探索（各桁は ABCDE に対応する）
for num in range(1<<5):
    # スコアと解いた問題の文字列
    score = 0
    moji = ''
    
    for shift in range(5):
        if 1 & (num>>shift) == 1:
            # 解いた問題のスコアを加算し、文字列を作っていく
            score += score_list[shift]
            moji = moji_list[shift] + moji
    
    # スコアと文字列をペアで記録
    if score > 0:
        ans.append([score, moji])

# スコアを基準として降順にソート、同スコアの場合は辞書順で小さくなるように
ans = sorted(ans, key=lambda x: (-x[0], x[1]))

for i in range(31):
    print(ans[i][1])

# 計算量 O(1)