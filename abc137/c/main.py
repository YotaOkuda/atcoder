from collections import defaultdict
from collections import Counter
import math as m

N = int(input())

dict_list = []
ans = 0

# 単語数分の連想配列をリストに格納
for i in range(N):
    dict_list.append(defaultdict(int))

# 各連想配列に各単語の各文字列を添字として出現回数を格納
for i in range(N):
    S = str(input())
    for s in S:
        dict_list[i][s] += 1

# 各連想配列をタプルに変換
tuple_list = [tuple(sorted(d.items())) for d in dict_list]
counter = Counter(tuple_list)   # 各タプルの出現回数を計算

for count in counter.values():
    if count >= 2:
        ans += m.comb(count, 2)     # 一致しているタプルの組み合わせを計算

print(ans)



'''
# 別解
from collections import defaultdict

N = int(input())
s_count = defaultdict(int)  # 文字列sが何個あるか
ans = 0

# 
for _ in range(N):
    s = ''.join(sorted(str(input())))   # 入力された文字をソート
    s_count[s] += 1     #入力された単語を添字として連想配列にインクリメント

for value in s_count.values():
    ans += (value*(value - 1))//2   # n個の中から２つ選ぶ組み合わせ、nC2

# こっちのが見やすいかも
# for key in s_count:
#     n = s_count[key]
#     ans += (n*(n - 1))//2

print(ans)
'''