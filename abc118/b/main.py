'''
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

exist = [0]*(M + 1)     # 0-Mまでのバケットを作成
for a in A:
    for i, n in enumerate(a):   # 文字列aに対してインデックスと要素を同時に取り出す
        if i == 0:          # 入力のkはスキップ
            continue
        exist[n] +=1        # 一致するバケットの要素にインクリメント

ans = 0
for n in exist:
     if n == N:     # 人数Nと一致しているバケット要素（N人全員が好きだと答えた食べ物があるとき）
         ans += 1   # 全員好きな食べ物のときインクリメント

print(ans)
'''



# リファクタリング
N, M = map(int, input().split())

exist = [0]*(M + 1)

for i in range(N):
    k, *a = list(map(int, input().split()))     # kとaを分ける→kをcontinueする処理がいらなくなる
    for n in a:     
        exist[n] += 1

ans = 0
for n in exist:
     if n == N:     # 人数Nと一致しているバケット要素（N人全員が好きだと答えた食べ物があるとき）
         ans += 1   # 全員好きな食べ物のときインクリメント

print(ans)

# 計算量O(NK+M)     K = リストの長さの平均