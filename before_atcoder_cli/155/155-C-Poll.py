from collections import defaultdict

N = int(input())

num = defaultdict(int)

for _ in range(N):
    s = input()
    num[s] += 1     # 連想配列にインクリメント

max_value = max(num.values())   # 一番多い出現回数を格納
for key in sorted(num):         # 辞書順に連想配列をソート
    if num[key] == max_value:   # 出現回数が一番多い文字列を出力
        print(key)

# 計算量O(NlogN) < 10^8
# N = max20 * 10^5