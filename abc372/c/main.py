N, Q = map(int, input().split())
S = input()

# 初期の'ABC'の数をカウント
count = S.count('ABC')

S = list(S)

for i in range(Q):
    X, C = input().split()
    X = int(X) - 1  # ベースインデックスへの変換
    
    # （文字変更前）影響する範囲の'ABC'をカウント
    minus = 0
    if X - 2 >= 0 and S[X-2:X+1] == ['A', 'B', 'C']:
        minus += 1
    if X - 1 >= 0 and S[X-1:X+2] == ['A', 'B', 'C']:
        minus += 1
    if X >= 0 and S[X:X+3] == ['A', 'B', 'C']:
        minus += 1
    
    # 文字変更
    S[X] = C
    
    # （文字変更後）影響する範囲の'ABC'をカウント
    plus = 0
    if X - 2 >= 0 and S[X-2:X+1] == ['A', 'B', 'C']:
        plus += 1
    if X - 1 >= 0 and S[X-1:X+2] == ['A', 'B', 'C']:
        plus += 1
    if X >= 0 and S[X:X+3] == ['A', 'B', 'C']:
        plus += 1
    
    # 変更前と後での'ABC'の数の変化を計算
    count -= minus
    count += plus
    print(count)

# 毎回文字列の全'ABC'をカウントするとTLEとなる
# 文字を変更すると影響の出る、[X-2:x+3]の範囲のみ'ABC'の増減をカウントする
# 文字の変更はリスト型に変換した文字列に代入することで計算量 O(1) にする（S[X] = C）

# 計算量 O(N + Q)



# TLE例
'''
for i in range(Q):
    X, C = input().split()
    X = int(X)
    S = S[:X - 1] + C + S[X:]  # 計算量をくうのでリスト型にして代入できるようにする
    print(S.count('ABC'))
'''