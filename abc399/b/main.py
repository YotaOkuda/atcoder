'''
<方針>
- 値 Pi の順位を出力すればよい
- 元のインデックスを保持しておくためのリストを用意し、P と降順にソートする
- ソートした P に順位をつけていく
- ひとつ前の値が同じであれば、同じ順位をつける
'''

N = int(input())
P = list(map(int, input().split()))

# インデックスを保持しておくためのリスト
index_list = [x for x in range(N)]
# 降順にソートする
P, index_list = zip(*sorted(zip(P, index_list), reverse=True))

# 順位付けを行う
ans = [1]
for i in range(1, N):
    if P[i] == P[i - 1]:
        ans.append(ans[-1])
    else:
        ans.append(i + 1)

# 元の並び順にソートする
index_list, ans = zip(*sorted(zip(index_list, ans)))

# 答えを出力
for i in range(N):
    print(ans[i])

# 計算量 O(N log N)