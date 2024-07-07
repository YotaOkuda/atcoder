N = int(input())
D = []
for _ in range(N):
    D.append(int(input()))

M = 101 # di <= 100より、バケット用の配列の要素数
exist = [0]*M   # 101までの要素数のバケットを用意
ans = 0

# Dの各要素の出現回数をカウント
for i in range(M):
    for d in D:
        if i == d:  # di = 1-101までのどれかと一致するときに,それに対応するバケットにカウントを追加
            exist[i] += 1   

# 出現回数が１以上の要素の合計を求める
for i in exist:
    if i >= 1:
        ans += 1

print(ans)

# 別解
# len(set(D)) 重複を考慮せず、リストDの中の異なる要素数を得ることができる