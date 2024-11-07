'''
<方針>
- N の各桁を格納したリストを作成する
- リストの合計値で S(N) を計算する
- S(N) で N が割り切れるか判定する
'''

N = int(input())

# 文字型にした N をループ処理して、各要素を数値型に変換してリストに格納
# 数値型は桁単位ではループできないため、文字型にする
N_list = [int(n) for n in str(N)]

# S(N) を求める
SN = sum(N_list)

# 割り切れるかを判定
if N % SN == 0:
    print('Yes')
else:
    print('No')
    
# 計算量 O(1)