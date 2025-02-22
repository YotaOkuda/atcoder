'''
<方針>
- 入力受け取り時に文字列の長さを一緒に配列として記録しておく
- 長さをキーとして配列をソートする
- 文字列を結合する
'''

N = int(input())
S = []
for _ in range(N):
    s = str(input())
    S.append([s, len(s)])  # [文字列, 長さ]を格納する

# 長さ（第 2 要素）をキーとしてソートする
sorted_S = sorted(S, key=lambda x:(x[1]))

# 文字列を結合
ans = ""
for s in sorted_S:
    ans += s[0]

print(ans)

# 計算量 O(N ^ 2)